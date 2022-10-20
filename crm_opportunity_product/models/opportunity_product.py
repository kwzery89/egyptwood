from odoo import api, fields, models, _
from odoo.exceptions import UserError

class CrmLeadProduct(models.Model):
    _name = 'crm.lead.product'

    product_id =  fields.Many2one('product.product',string='Product')
    description = fields.Text(string='Description')
    qty = fields.Float(string='Ordered Qty',default=1.0)
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure')
    price_unit = fields.Float(string='Unit Price')
    tax_id = fields.Many2many('account.tax', string='Taxes')
    lead_id = fields.Many2one('crm.lead')
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True,
        default=lambda self: self.env.company)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string="Company Currency",
        related='company_id.currency_id')
    price_subtotal = fields.Monetary(compute='_compute_amount', currency_field='currency_id', string='Subtotal', store=True)


    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.description = self.product_id.name
            self.price_unit = self.product_id.lst_price
            self.product_uom = self.product_id.uom_id.id
            self.tax_id = self.product_id.taxes_id.ids

    @api.depends('qty', 'price_unit')
    def _compute_amount(self):
        """
        Compute the amounts of the products line.
        """
        for rec in self:
            rec.price_subtotal = rec.qty * rec.price_unit
            
        
class CrmLead(models.Model):
    _inherit = 'crm.lead'

    lead_product_ids = fields.One2many('crm.lead.product','lead_id',string='Products For Quotation')
    service_type = fields.Many2one(comodel_name='contract.type', string='Service Type')
    project_manager_id = fields.Many2one(comodel_name='hr.employee', string='Project Manager')
    amount_total = fields.Float(string='Total', compute='compute_amount_total', readonly=True, store=True)

    @api.depends('lead_product_ids')
    def compute_amount_total(self):
        total = 0.0
        for rec in self:
            for line in rec.lead_product_ids:
                total += line.price_subtotal
                rec.amount_total = total
                
    def action_create_quotation(self):
        order_lines = []
        sale_order = self.env['sale.order']

        for line in self.lead_product_ids:
            order_lines.append((0,0,{
                'product_id': line.product_id.id,
                'name': line.description,
                'product_uom_qty':line.qty,
                'product_uom': line.product_uom.id,
                'price_unit': line.price_unit,
                'tax_id':[(6, 0, line.tax_id.ids)]
            }))

        if self.partner_id:
            vals = ({
                'partner_id':self.partner_id.id,
                'team_id': self.team_id.id,
                'campaign_id': self.campaign_id.id,
                'medium_id': self.medium_id.id,
                'source_id': self.source_id.id,
                'opportunity_id': self.id,
                'order_line':order_lines,
            })
            so = sale_order.create(vals)
            
        else:
            raise UserError('In order to create sale order, Customer field should not be empty!')


        return {
            'name': "Create Sale Quotation",
            'type': 'ir.actions.act_window',
            'view_type': 'list',
            'view_mode': 'list',
            'views': [[False, 'list'], [False, 'form']],
            'res_model': 'sale.order',
            'target': 'current',
            'domain': [('id', '=', so.id)],
        }
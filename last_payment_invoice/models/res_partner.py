# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta


class ResPartner(models.Model):
    _inherit = "res.partner"

    birthday = fields.Date('Date of Birth')
    age = fields.Char(compute='_get_age', string='Age')
    last_payment = fields.Monetary(string="Last Payment", readonly=True, compute="get_last_payment", copy=False)
    last_payment_date = fields.Date(string="Last Payment Date", readonly=True, compute="get_last_payment", copy=False)
    last_invoice = fields.Monetary(string="Last Invoice", readonly=True, compute="get_last_invoice", copy=False)
    last_invoice_date = fields.Date(string="Last Invoice Date", readonly=True, compute="get_last_invoice", copy=False)

    def get_last_payment(self):
        for partner in self:
            payments_ids = self.env['account.payment'].search([('partner_id', '=', partner.id), ('state', '=', 'posted')])
            payment = payments_ids and max(payments_ids)
            if payment:
                partner.last_payment_date = payment.payment_date
                partner.last_payment = payment.amount

    def get_last_invoice(self):
        for partner in self:
            invoice_ids = self.env['account.invoice'].search([('partner_id', '=', partner.id),
                                                              ('state', 'not in', ['draft', 'cancel'])])
            invoice = invoice_ids and max(invoice_ids)
            if invoice:
                partner.last_invoice = invoice.amount_total
                partner.last_invoice_date = invoice.date_invoice

    @api.depends('birthday')
    def _get_age(self):

        now = datetime.now()
        years_months_days = ""
        years = ""

        for r in self:
            if r.birthday and r.is_company is False:
                p_dob = datetime.strptime(str(r.birthday), '%Y-%m-%d')
                delta = relativedelta.relativedelta(now, p_dob)
                years_months_days = str(delta.years) + "y " + str(delta.months) + "m " + str(delta.days) + "d "
                years = str(delta.years)
            r.age = years
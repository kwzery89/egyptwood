# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta


class ResPartner(models.Model):
    _inherit = "res.partner"

    last_payment = fields.Monetary(string="Last Payment", readonly=True, store=True, compute="get_last_payment",
                                   copy=False)
    last_payment_date = fields.Date(string="Last Payment Date", readonly=True, store=True, compute="get_last_payment",
                                    copy=False)
    last_invoice = fields.Monetary(string="Last Invoice", readonly=True, store=True, compute="get_last_invoice", copy=False)
    last_invoice_date = fields.Date(string="Last Invoice Date", readonly=True, store=True, compute="get_last_invoice", copy=False)

    @api.depends('name')
    def get_last_payment(self):
        for partner in self:
            payments_ids = self.env['account.payment'].search(
                [('partner_id', '=', partner.id), ('state', '=', 'posted')])
            payment = payments_ids and max(payments_ids)
            if payment:
                partner.last_payment_date = payment.payment_date
                partner.last_payment = payment.amount

    @api.depends('name')
    def get_last_invoice(self):
        for partner in self:
            invoice_ids = self.env['account.move'].search([('partner_id', '=', partner.id),
                                                              ('state', 'not in', ['draft', 'cancel'])])
            invoice = invoice_ids and max(invoice_ids)
            if invoice:
                partner.last_invoice = invoice.amount_total
                partner.last_invoice_date = invoice.invoice_date


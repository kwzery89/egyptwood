# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2021 Cloudroits (info.cloudroits@gmail.com)
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models

#Display amount in words in Sale order
class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def _compute_amount2words(self):
        for rec in self:
                rec.amount_words = str(rec.currency_id.amount_to_text(rec.amount_total))

    amount_words = fields.Char(string="Total amount in words: ", help=
        "Total amount in words is automatically generated by the system", compute='_compute_amount2words')
# -*- coding: utf-8 -*-
{
    'name': 'Display Amount In Words in quotations, invoices and purchase orders',
    'version': '15.0.0.0',
    'author': 'Cloudroits',
    'summary': 'Display Amount In Words in quotations, invoices and purchase orders, both in forms as well as reports',
    'description': """This module displays Total Amount In Words in quotations, invoices and purchase orders, both in forms as well as reports.""",
    'category': 'Sales',
    'website': 'https://www.cloudroits.com/',
    'license': 'AGPL-3',
    'depends': ['sale_management','purchase'],
    'data': [
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/invoice_view.xml',
        'report/sale_order_report.xml',
        'report/purchase_order_report.xml',
        'report/invoice_report.xml',
    ],
    'qweb': [],
    'images': ['static/description/odoo_amount_in_words_banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
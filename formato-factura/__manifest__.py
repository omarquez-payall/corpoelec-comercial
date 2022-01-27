# -*- coding: utf-8 -*-
{
    'name': "formato-factura",

    'summary': """
        Modulo implementado para los procesos de emision de factura""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Payall",
    'website': 'https://payall.com.ve/',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_accountant'],

    # always loaded
    'data': [
        'security/invoices_images_security.xml',
        'security/ir.model.access.csv',
        'data/invoices_images.xml',
        'views/invoice_images.xml',
        'views/invoice_images_inherit.xml',
        'views/account_move_inherit_view.xml',
        'views/res_partner_inherit.xml',
        'report/external_layout_background_inherit.xml',
        'report/report_invoice_document.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

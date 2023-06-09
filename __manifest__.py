# -*- coding: utf-8 -*-
{
    'name': "proyecto3",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'website_sale'],

    # always loaded
    'data': [
        'security/sells_security.xml',
        'security/ir.model.access.csv',
        'views/wizard_generator_view.xml',
        'views/sale_line_view.xml',
        'views/invoice_line_view.xml',
        'views/codes_sells_view.xml',
        'views/invoice_sells_view.xml',
        'views/report.xml',
        'views/report_invoices.xml',
        'views/key_code_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

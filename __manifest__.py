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
    'depends': ['base', 'website','website_sale'],

    'assets': {
        'web.assets_frontend': [
            'website_sale/static/src/js/website_sale.js',
        ],
    },

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/wizard_generator_view.xml',
        'views/sale_line_view.xml',
        'views/codes_sells_view.xml',
        'views/key_code_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

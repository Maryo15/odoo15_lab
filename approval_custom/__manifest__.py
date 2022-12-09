# -*- coding: utf-8 -*-
{
    'name': "Custom-Approvals",

    # 'summary': """
    #     Short (1 phrase/line) summary of the module's purpose, used as
    #     subtitle on modules listing or apps.openerp.com""",

    # 'description': """
    #     Long description of module's purpose
    # """,

    'author': "Indasoge-Alphasys",
    'website': "http://www.alphasys.com.bo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Localizations',
    'version': '0.9',

    # any module necessary for this one to work correctly
    'depends': ['base', 'approvals'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/approval_category_view_inherit.xml',
        'views/approval_request_view_inherit.xml',
        'views/approval_category_approver_view_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}

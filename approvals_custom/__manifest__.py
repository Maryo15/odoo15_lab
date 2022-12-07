{
    'name': 'Approvals Custom',
    'version': '15.0.1.0.0',
    'category': 'Approvals Custom',
    'author': '',
    'company': '',
    'maintainer': '',
    'website': " ",
    'summary': """Approvals Custom""",
    'description': """Approvals Custom, Odoo15, Odoo 15""",
    'depends': ["base","approvals","mass_mailing"],
    'data': [
        "security/ir.model.access.csv",
        "data/approvals_custom.xml",
        "views/approvals_template.xml",
        "views/approvals_custom_wizard.xml",
        "views/approval_wizard.xml",
    ],
    
    'application': True,
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,
    
}
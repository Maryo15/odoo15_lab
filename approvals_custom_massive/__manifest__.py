{
    'name': 'Approvals Custom - Massive',
    'version': '15.0.1.0.0',
    'category': 'Approvals Custom',
    'author': '',
    'company': '',
    'maintainer': '',
    'website': " ",
    'summary': """Approvals Custom""",
    'description': """Approvals Custom, Odoo15, Odoo 15""",
    'depends': ["base", "approvals", "approval_custom", "mass_mailing"],
    'data': [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "data/approvals_custom.xml",
        "views/approvals_template.xml",
        "views/approval_request_view_form.xml",
        "views/approvals_wizard.xml",
        "views/action_wizard.xml",
    ],

    'application': True,
    'installable': True,
    'license': 'AGPL-3',
    'auto_install': False,

}

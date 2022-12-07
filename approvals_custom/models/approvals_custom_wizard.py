from odoo import models, fields, api
from datetime import timedelta, datetime, date

class ApprovalsCustomWizard(models.Model):
    _name = 'approvals.custom.wizard'
    _description = 'Approvals Custom Wizard'
    test_field = fields.Char(string = 'Test Field')

    """def open_approvals_custom_wizard(self):
        for rec in self:
            approvals_custom_wizard = self.env['approvals_custom_wizard'].search([('approvals_custom_wizard_id','=',rec.name)]).ids
            view_id = self.env.ref('approvals_custom.view_approvals_custom_wizard_tree').id
            return {
                'name': 'Approvals custom wizard',
                "type": "ir.actions.act_window",
                "res_model": "approvals.custom.wizard",
                "views": [[False, "tree"], [False, "form"]],
                "domain": [["id", "in", approvals_custom_wizard]],
            }"""
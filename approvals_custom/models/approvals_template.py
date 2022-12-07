from odoo import models, fields, api
from datetime import timedelta, datetime, date


class ApprovalsTemplate(models.Model):
    _name='approvals.template'

    name = fields.Char('name')

    """def open_approvals_template(self):
        for rec in self:
            approvals_template = self.env['approvals_template'].search([('approvals_template_id','=',rec.name)]).ids
            view_id = self.env.ref('approvals_custom.view_approvals_template_tree').id
            return {
                'name': 'Approvals template',
                "type": "ir.actions.act_window",
                "res_model": "approvals.template",
                "views": [[False, "tree"], [False, "form"]],
                "domain": [["id", "in", approvals_template]],
            }"""
 

from odoo import _, models, fields, api
from datetime import timedelta, datetime, date


class ApprovalsTemplate(models.Model):
    _name = 'approvals.template'

    name = fields.Char('Tipo de talento')
    mail_template_id = fields.Many2one(
        'mailing.mailing', string='Mail Template')

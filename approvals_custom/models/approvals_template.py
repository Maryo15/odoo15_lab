from odoo import models, fields, api
from datetime import timedelta, datetime, date


class ApprovalsTemplate(models.Model):
    _name='approvals.template'

    name = fields.Char('name')
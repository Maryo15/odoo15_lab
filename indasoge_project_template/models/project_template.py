
from odoo import models, fields, api
from datetime import timedelta, datetime, date


class ProjectTemplate(models.Model):
    _name='project.template'

    name = fields.Char('name')
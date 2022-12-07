from odoo import models, fields
from datetime import timedelta, datetime, date

class ResultFormat(models.Model):
    _name ='result.format'
    _rec_name = 'code'
    _description = "Result Format"



from odoo import _, models, fields, api
from datetime import timedelta, datetime, date


class MailMail(models.Model):
    _inherit = 'mail.mail'

    request_id = fields.Many2one('approval.request', string='Request')


class MassMailing(models.Model):
    _inherit = 'mailing.mailing'

    request_id = fields.Many2one('approval.request', string='Request')

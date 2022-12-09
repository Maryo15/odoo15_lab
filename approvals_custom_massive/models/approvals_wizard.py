import logging
from odoo import models, fields, api
from datetime import timedelta, datetime, date
_logger = logging.getLogger(__name__)


class ApprovalsWizard(models.TransientModel):
    _name = 'approvals.wizard'
    _description = 'Approvals Wizard'

    template_id = fields.Many2one('approvals.template', string='Template')
    employee_ids = fields.Many2many('hr.employee', string='Partner')
    request_id = fields.Many2one('approval.request', string='Request')

    def send_massive_invoice_request(self):
        for rec in self:
            employee_ids = []
            for e in rec.employee_ids:
                employee_ids.append(e.work_email)
            mailing = rec.template_id.mail_template_id.copy()
            mailing.request_id = rec.request_id.id
            rec.request_id.type_mail = '0'
            rec.template_id.mail_template_id.body_arch = rec.template_id.mail_template_id.body_arch.format(
                proyecto=rec.request_id.project.name if rec.request_id.project else '',
                defined_hours=rec.request_id.defined_hours if rec.request_id.defined_hours else '',
                worked_hours=rec.request_id.worked_hours if rec.request_id.worked_hours else '',
                extra_hours=rec.request_id.extra_hours if rec.request_id.extra_hours else ''
            )
            mailing.mailing_domain = "[['email', 'in', {}]]".format(
                employee_ids)

    def send_invoice_request(self):
        for rec in self:
            for e in rec.employee_ids:
                body = rec.template_id.mail_template_id.body_arch.format(
                    proyecto=rec.request_id.project.name if rec.request_id.project else '',
                    defined_hours=rec.request_id.defined_hours if rec.request_id.defined_hours else '',
                    worked_hours=rec.request_id.worked_hours if rec.request_id.worked_hours else '',
                    extra_hours=rec.request_id.extra_hours if rec.request_id.extra_hours else '')
                mail_values = {
                    'subject': '{} - {}'.format(rec.request_id.name, rec.template_id.name),
                    'body_html': body,
                    'email_to': e.work_email,
                    'request_id': rec.request_id.id,
                }
                mail = self.env['mail.mail'].create(mail_values)
            rec.request_id.type_mail = '1'

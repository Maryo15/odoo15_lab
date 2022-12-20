import logging
from odoo import models, fields, api
from datetime import timedelta, datetime, date
_logger = logging.getLogger(__name__)


class ApprovalsWizard(models.TransientModel):
    _name = 'approvals.wizard'
    _description = 'Approvals Wizard'

    template_id = fields.Many2one('approvals.template', string='Template')
    request_ids = fields.Many2many(
        'approval.request', string='Request', readonly=True)
    employee_ids = fields.Many2many(
        'hr.employee', string='Partner', store=True, readonly=False)

    @api.onchange('template_id')
    def _onchange_template_id(self):
        for rec in self:
            rec.request_ids = self.env['approval.request'].browse(
                self._context.get('active_ids', []))
            _logger.info('rec.request_ids*****{}'.format(rec.request_ids))
            rec.employee_ids = rec.request_ids.mapped(
                'asigned_employe_ids')

    def send_invoice_request(self):
        approval_request = self.env['approval.request'].browse(
            self._context.get('active_ids', []))
        for rec in self:
            for request in approval_request:
                request_employee_ids = request.asigned_employe_ids
                for e in request_employee_ids:
                    if e in rec.employee_ids:
                        body = rec.template_id.mail_template_id.body_arch.format(
                            proyecto=request.project if request.project else '',
                            defined_hours=request.defined_hours if request.defined_hours else '',
                            worked_hours=request.worked_hours if request.worked_hours else '',
                            extra_hours=request.extra_hours if request.extra_hours else '')
                        _logger.info('e*****{}'.format(e))
                        mail_values = {
                            'subject': '{} - {}'.format(request.name, rec.template_id.name),
                            'body_html': body,
                            'email_to': e.work_email if e.work_email else '',
                            'request_id': request.id,
                        }
                        mail = self.env['mail.mail'].create(mail_values)

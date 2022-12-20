import logging
from odoo import _, models, fields, api
from datetime import timedelta, datetime, date
_logger = logging.getLogger(__name__)


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    mail_count = fields.Integer(compute='compute_count')

    def compute_count(self):
        for record in self:
            record.mail_count = self.env['mail.mail'].search_count(
                [('request_id', '=', record.id)])

    def get_mails(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Massive Mail',
            'view_mode': 'tree,form',
            'res_model': 'mail.mail',
            'domain': [('request_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def open_wizard_to_process(self):
        view = self.env.ref(
            'approvals_custom_massive.approvals_wizard_view_form')
        
        return {
            'name': _('Enviar correos'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'approvals.wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': {'default_request_id': self.id},
            # 'res_id': wiz.id,
        }

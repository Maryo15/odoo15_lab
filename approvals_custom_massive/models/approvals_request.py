from odoo import _, models, fields, api
from datetime import timedelta, datetime, date


class ApprovalRequest(models.Model):
    _inherit = 'approval.request'

    mail_count = fields.Integer(compute='compute_count')
    type_mail = fields.Selection([
        ('0', 'massive_mail'),
        ('1', 'mail')
    ], string='Type Mails')

    def compute_count(self):
        for record in self:
            if self.type_mail == '1':
                record.mail_count = self.env['mail.mail'].search_count(
                    [('request_id', '=', self.id)])
            if self.type_mail == '0':
                record.mail_count = self.env['mailing.mailing'].search_count(
                    [('request_id', '=', self.id)])

    def get_mails(self):
        self.ensure_one()
        if self.type_mail == '1':
            return {
                'type': 'ir.actions.act_window',
                'name': 'Mail',
                'view_mode': 'tree',
                'res_model': 'mail.mail',
                'domain': [('request_id', '=', self.id)],
                'context': "{'create': False}"
            }
        if self.type_mail == '0':
            return {
                'type': 'ir.actions.act_window',
                'name': 'Massive Mail',
                'view_mode': 'tree',
                'res_model': 'mailing.mailing',
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

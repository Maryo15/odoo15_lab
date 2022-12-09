from odoo import api, fields, models
from odoo.exceptions import UserError, Warning, ValidationError

class ApprovalApprover(models.Model):
    _inherit = 'approval.approver'
    _description = 'Approval Approver Inherit'

    def _get_approver_sequence(self):
        find_category_approver = None
        for cat_approver in self.request_id.category_id.approver_ids:
            for user in self.user_id:
                if cat_approver.user_id.id == user.id:
                    find_category_approver = cat_approver
        if find_category_approver:    
            self.sequence_number = find_category_approver
        else:
            self.sequence_number = 0
    sequence_number = fields.Integer(string='Secuencia', compute="_get_approver_sequence")
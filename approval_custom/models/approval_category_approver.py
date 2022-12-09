from odoo import api, fields, models
from odoo.exceptions import UserError, Warning, ValidationError

class ApprovalCategoryApprover(models.Model):
    _inherit = 'approval.category.approver'
    _description = 'Approval Category Approver Inherit'
    
    # @api.depends('category_id.current_sequence')
    # def _get_current_sequence(self):
    #     self.sequence_number = self.category_id.current_sequence
    # sequence_number = fields.Integer(string='Secuencia', compute='_get_current_sequence', store=True)

    sequence_number = fields.Integer(string='Secuencia')

    @api.onchange("required")
    def _onchange_required_seq_number(self):
        current_seq = self.category_id.current_sequence
        if self.user_id and self.category_id.ext_payment_flag:
            if self.required:
                current_seq = current_seq + 1
            else:
                if current_seq > 0:
                    current_seq = current_seq - 1
            self.category_id.write({'current_sequence': current_seq})
            self.sequence_number = current_seq
    
    @api.onchange("sequence_number")
    def _onchange_sequence_number(self):
        if self.sequence_number < 0:
            raise ValidationError("No se puede asignar una secuencia negativa")
    
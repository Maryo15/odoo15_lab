from odoo import api, fields, models
from odoo.exceptions import UserError, Warning, ValidationError
from datetime import datetime, timedelta

MONTHS = [
    ('01', 'Enero'),
    ('02', 'Febrero'),
    ('03', 'Marzo'),
    ('04', 'Abril'),
    ('05', 'Mayo'),
    ('06', 'Junio'),
    ('07', 'Julio'),
    ('08', 'Agosto'),
    ('09', 'Septiembre'),
    ('10', 'Octubre'),
    ('11', 'Noviembre'),
    ('12', 'Diciembre')]

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'
    _description = 'Approval Request Inherit'


    ext_payment_flag = fields.Boolean(related="category_id.ext_payment_flag", string="Es Pago Externo")

    has_defined_hours = fields.Selection(related="category_id.has_defined_hours")
    has_worked_hours = fields.Selection(related="category_id.has_worked_hours")
    has_extra_hours = fields.Selection(related="category_id.has_extra_hours")

    
    asigned_employe_ids = fields.Many2many(comodel_name='hr.employee', string='Talento')

    payment_month = fields.Selection( MONTHS ,string='Mes Periodo', default="01", required=True)

    project = fields.Char(string='Proyecto')

    notes = fields.Char(string='Notas')
    
    


    # @api.depends('payment_month')
    # def _set_payment_period(self):
    #     year_now = str(datetime.now().year)
    #     self.payment_period = self.payment_month + "/" + year_now
    # payment_period = fields.Char(string='Periodo', compute='_set_payment_period', store=True )
    payment_period = fields.Char(string='Periodo')

    # def _get_approver_ids(self):
    #     self.required_approvers = self.category_id.approver_ids.search([('sequence_number' ,'!=', 0)])
    # required_approvers = fields.Many2many(comodel_name='approval.category.approver', string='Autorizadores requeridos')

    required_approvers = fields.One2many(related="category_id.approver_ids", string="Autorizadores")
    
    defined_hours = fields.Float(string='Horas Pactadas', digits=(8,2))
    worked_hours = fields.Float(string='Horas Trabajadas', digits=(8,2))
    extra_hours = fields.Float(string='Horas Extra', digits=(8,2))

    approval_counter = fields.Integer(string='Número actual Autorización', default = 0, readonly=True)
    approval_min = fields.Integer(related="category_id.approval_minimum", string='Número mínimo Autorización')
    
    @api.constrains('defined_hours')
    def _check_defined_hours(self):
        for record in self:
            if fields.Float.compare(self.defined_hours,0.00,2) < 0:
                raise ValidationError("Los campos de horas no pueden tener valores negativos")

    @api.constrains('worked_hours')
    def _check_worked_hours(self):
        for record in self:
            if fields.Float.compare(self.worked_hours,0.00,2) < 0:
                raise ValidationError("Los campos de horas no pueden tener valores negativos")

    @api.constrains('extra_hours')
    def _check_extra_hours(self):
        for record in self:
            if fields.Float.compare(self.extra_hours,0.00,2) < 0:
                raise ValidationError("Los campos de horas no pueden tener valores negativos")
    

    def action_confirm(self):
        if fields.Float.compare(self.defined_hours,0.00,2) < 0 or fields.Float.compare(self.worked_hours,0.00,2) < 0 or fields.Float.compare(self.extra_hours,0.00,2) < 0:
            raise ValidationError("Los campos de horas no pueden tener valores negativos")
        super(ApprovalRequest, self).action_confirm()
    
    def action_approve(self, approver=None):
        check_approver = 0
        for approver in self.category_id.approver_ids:
            if approver.user_id.id == self.env.user.id:
                if approver.sequence_number == self.approval_counter + 1:
                    check_approver = 1
                    self.approval_counter = self.approval_counter + 1
        if check_approver:
            super(ApprovalRequest, self).action_approve()
        else:
            raise ValidationError("El presente usuario no es autorizador o depende de otro para aprobar")
    
    def action_cancel(self):
        ##TODO Consultar si el propietario puede ser aprobador de la misma forma
        if self.request_owner_id.id == self.env.user.id:
            raise ValidationError("El propietario no puede cancelar la presente entrada")
        else:
            check_approver = 0
            for approver in self.category_id.approver_ids:
                if approver.user_id.id == self.env.user.id:
                    check_approver = 1
            if not check_approver:
                raise ValidationError("Las entradas solo pueden ser canceladas por los aprobadores")
            else:
                self.approval_counter = 0
                super(ApprovalRequest, self).action_cancel()
    
    def action_draft(self):
        if not self.request_owner_id.id == self.env.user.id:
            raise ValidationError("Solo el propietario puede editar una entrada cancelada")
        super(ApprovalRequest, self).action_draft()
    
    @api.onchange("payment_month")
    def _onchange_payment_month(self):
        year_now = str(datetime.now().year)
        self.payment_period = self.payment_month + "/" + year_now
    
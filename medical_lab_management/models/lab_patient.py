from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class   Profesional(models.Model):
    _name = 'profesional'
    name = fields.Char('name')

class   Especialidad(models.Model):
    _name = 'especialidad'
    name = fields.Char('name')

class   TipoSeguro(models.Model):
    _name = 'tipo.seguro'
    name = fields.Char('name')

class LabPatient(models.Model):
    _name = 'lab.patient'
    _description = 'Patient'    
    partner_id = fields.Many2one('res.partner',
                                 string='Partner',
                                 required=True)
    patient_image = fields.Binary(string='Photo') 
    patient_id = fields.Char(string='Patient ID',
                             readonly=True)
    name = fields.Char(string='Patient',
                       readonly=True,
                       default=lambda self: _('New'))
    title = fields.Selection([
         ('ms', 'Sra.'),
         ('mister', 'Sr.'),
    ],string='Title',
      default='mister',
      required=True)
    emergency_contact = fields.Many2one(
        'res.partner', string='Emergency Contact')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ('ot', 'Other')], 'Gender', required=True)
    dob = fields.Date(string='Date Of Birth', required=True)
    age = fields.Char(string='Age', compute='compute_age')
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Blood Group') 
    telefono_acompanante = fields.Char(string="Telefono acompañante",
                                       required=True)
    #descripcion = fields.Text(string='Descripcion')
    date = fields.Datetime(string='Date Requested',
                           default=lambda s: fields.Datetime.now(),
                           invisible=True)
    phone = fields.Char(string="Phone", required=True)
    email = fields.Char(string="Email", required=True)
    nacionalidad = fields.Char(string='Nacionalidad', size=64)
    condicion = fields.Selection(
        [('ur', 'Urgente'), ('ru', 'Rutina'),
         ], 'Condicion', required=True)
    fecha_de_registro = fields.Date(string='Fecha de registro',
                                    required=True)
    dni = fields.Char(string='DNI', size=64)
    historia_clinica = fields.Text(string='Observación')

    tipo_seguro_id = fields.Selection(
        [('sis', 'SIS'), ('essa', 'EsSalud'),
         ], 'Tipo seguro', required=True)
    especialidad_id = fields.Many2one('especialidad', string='Especialidad')
    profesional_id = fields.Many2one('profesional', string='Profesional')

    def compute_age(self):
        for data in self:
            if data.dob:
                dob = fields.Datetime.from_string(data.dob)
                date = fields.Datetime.from_string(data.date)
                delta = relativedelta(date, dob)
                data.age = str(delta.years) + ' years'
            else:
                data.age = ''

    #@api.onchange('partner_id')
    def onchange_form(self):
        for record in self:
            if record.dni:
               record.partner_id.vat = record.dni
            if record.telefono_acompanante:
                record.partner_id.phone = record.telefono_acompanante
            if record.phone:
                record.partner_id.mobile = record.phone
            if record.email:
                record.partner_id.email = record.email
            

    @api.model
    def create(self, vals):
        sequence = self.env['ir.sequence'].next_by_code('lab.patient')
        vals['name'] = sequence or _('New')
        result = super(LabPatient, self).create(vals)
        return result

    @api.onchange('patient')
    def detail_get(self):
        self.phone = self.partner_id.phone
        self.email = self.partner_id.email
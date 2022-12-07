from odoo import models, fields, api
from datetime import timedelta, datetime, date

class ApprovalsWizard(models.Model):
    _name = 'approvals.wizard'
    _description = 'Approvals Wizard'
    test_field = fields.Char(string = 'Test Field')

def action_done(self):
    records = self.env['approvals.wizard'].browse(self.env.context.get('active_ids'))
    for rec in records: 
        rec.write({'state' : 'done'})

def create_wizard(self):
   wizard = self.env['test.model.wizard'].create({'test_field': self.name})
   return {'name': ('Test Wizard'),
   type:'ir.actions.act_window',
   'res_model': 'test.model.wizard',
   'view_mode': 'form',
   'res_id': wizard.id,
   'target': 'new'
}
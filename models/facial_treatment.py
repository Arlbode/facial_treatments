from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class FacialTreatment(models.Model):
    _name = 'facial.treatment'
    _description = 'Tratamiento Facial'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'  # Mostrar tratamientos más recientes primero

    name = fields.Char(string='Referencia', default='Nuevo', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    date = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    next_appointment = fields.Datetime(string='Próxima Cita')
    product_ids = fields.Many2many('product.product', string='Productos Usados')
    notes = fields.Text(string='Observaciones')
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('done', 'Completado'),
        ('cancel', 'Cancelado')
    ], default='draft', string='Estado')

    @api.constrains('date', 'next_appointment')
    def _check_dates(self):
        for record in self:
            if record.next_appointment and record.date and record.next_appointment < record.date:
                raise ValidationError("La próxima cita no puede ser anterior a la fecha del tratamiento.")

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('facial.treatment') or 'Nuevo'
        return super().create(vals)

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel', 'next_appointment': False})

    def action_schedule_appointment(self):
        self.ensure_one()
        if self.next_appointment:
            event = self.env['calendar.event'].create({
                'name': f'Cita de seguimiento para {self.partner_id.name}',
                'start': self.next_appointment,
                'stop': self.next_appointment + timedelta(hours=1),
                'partner_ids': [(4, self.partner_id.id)],
            })
            self.message_post(body=f'Se ha agendado una cita para el {self.next_appointment}.')
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'calendar.event',
                'view_mode': 'form',
                'res_id': event.id,
                'target': 'new',
            }


class ResPartner(models.Model):
    _inherit = 'res.partner'
    treatment_ids = fields.One2many('facial.treatment', 'partner_id', string='Tratamientos')
from odoo import models, fields, api

class FacialTreatment(models.Model):
    _name = 'facial.treatment'
    _description = 'Tratamiento Facial'
    _inherit = ['mail.thread', 'mail.activity.mixin']

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

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('facial.treatment') or 'Nuevo'
        return super().create(vals)

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

class ResPartner(models.Model):
    _inherit = 'res.partner'
    treatment_ids = fields.One2many('facial.treatment', 'partner_id', string='Tratamientos')

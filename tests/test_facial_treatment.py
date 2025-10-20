from odoo.tests.common import TransactionCase
from datetime import datetime, timedelta

class TestFacialTreatment(TransactionCase):
    def setUp(self):
        super(TestFacialTreatment, self).setUp()
        self.partner = self.env['res.partner'].create({'name': 'Test Partner'})
        self.treatment = self.env['facial.treatment'].create({
            'partner_id': self.partner.id,
            'date': datetime.now(),
            'next_appointment': datetime.now() + timedelta(days=30)
        })

    def test_cancel_clears_next_appointment(self):
        self.treatment.action_cancel()
        self.assertFalse(self.treatment.next_appointment, "Canceling a treatment should clear the next appointment date.")

    def test_schedule_appointment(self):
        self.treatment.action_done()
        self.treatment.action_schedule_appointment()
        event = self.env['calendar.event'].search([('name', '=', f'Cita de seguimiento para {self.partner.name}')])
        self.assertTrue(event, "Scheduling an appointment should create a calendar event.")
        self.assertEqual(event.start, self.treatment.next_appointment, "The event should be scheduled for the next appointment date.")
        self.assertEqual(event.stop, self.treatment.next_appointment + timedelta(hours=1), "The event should end one hour after the start.")
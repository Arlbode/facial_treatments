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
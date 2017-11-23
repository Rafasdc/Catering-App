from django.test import TestCase
from django.core import mail
from .models import Notify

class EmailTest(TestCase):

   def test_send_email(self):
   		Notify.sendEmail(['jasonsanche@gmail.com'])
   		self.assertEqual(len(mail.outbox), 1)
   		self.assertEqual(mail.outbox[0].subject,'Some subject')
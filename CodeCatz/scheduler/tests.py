from django.test import TestCase
from django.apps import apps
from scheduler.apps import SchedulerConfig
from django.apps import AppConfig
from django.core import mail
from django.conf import settings
from django.test.utils import override_settings
from django.contrib.auth.models import User
from scheduler import *
from events.models import *
import datetime
import time

@override_settings(EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend')

class SchedulerConfigTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		test_user = User()
		test_user.username = 'BobTest'
		test_user.save()
		test_date = datetime.datetime.today() + datetime.timedelta(days=7)
		# test_startTime = datetime.datetime.today() + datetime.timedelta(days=7)
		Event.objects.create(
			user = test_user,
			date = test_date,
			# startTime = test_startTime,
			numGuests = 200,
			location = 'anywhere'
		)

	def test_apps(self):
		self.assertEqual(SchedulerConfig.name, "scheduler")

	def test_scheduler_email(self):
		event=Event.objects.get(id=1)
		SchedulerConfig.ready(event)
		self.assertEqual(len(mail.outbox), 1)

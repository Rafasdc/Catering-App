from django.test import TestCase
from django.contrib.auth.models import User
from events.models import *

class EventTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		test_user = User()
		test_user.username = 'BobTest'
		test_user.save()
		Event.objects.create(
			user = test_user,
			numGuests = 200,
			location = 'anywhere'
		)

	def test_event_numGuests_value(self):
		event=Event.objects.get(id=1)
		self.assertEquals(event.numGuests,200)

	def test_event_location(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('numGuests')
		self.assertEquals(event.location,'anywhere')

	def test_event_user_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('user').verbose_name
		self.assertEquals(field_label,'user')

	def test_object_name_is_username_comma_numGuests(self):
		event=Event.objects.get(id=1)
		expected_object_name = '%s, %s' % (event.user.username, event.numGuests)
		self.assertEquals(expected_object_name,'BobTest, 200')


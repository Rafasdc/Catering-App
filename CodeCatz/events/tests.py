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

	def test_event_location_value(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('numGuests')
		self.assertEquals(event.location, 'anywhere')

	def test_event_type_value(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('event_type')
		self.assertEquals(event.event_type,field_label.default)

	def test_event_user_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('user').verbose_name
		self.assertEquals(field_label,'user')

	def test_event_NumGuests_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('numGuests').verbose_name
		self.assertEquals(field_label,'Number of Guests')

	def test_event_date_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('date').verbose_name
		self.assertEquals(field_label,'date')

	def test_event_event_type_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('event_type').verbose_name
		self.assertEquals(field_label,'event type')

	def test_event_startTime_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('startTime').verbose_name
		self.assertEquals(field_label,'startTime')

	def test_event_location_field(self):
		event=Event.objects.get(id=1)
		field_label = event._meta.get_field('location').verbose_name
		self.assertEquals(field_label,'location')

	def test_object_name_is_username_comma_numGuests(self):
		event=Event.objects.get(id=1)
		expected_object_name = '%s, %s' % (event.user.username, str(event.numGuests) + ' guests')
		self.assertEquals(expected_object_name, str(event))


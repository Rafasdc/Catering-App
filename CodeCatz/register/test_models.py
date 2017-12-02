from django.test import TestCase
from .models import *

class UserProfileTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		test_user = User()
		test_user.first_name = 'Bob'
		test_user.last_name = 'Test'
		test_user.email = 'bob@test.com'
		test_user.save()
		test_profile = UserProfile.objects.get(id=test_user.id)
		test_profile.phone='222-222-2222'
		test_profile.address='Test'
		test_profile.save()

	def test_address_label(self):
		profile = UserProfile.objects.get(id=1)
		field_label = profile._meta.get_field('address').verbose_name
		self.assertEquals(field_label, 'address')

	def test_phone_label(self):
		profile = UserProfile.objects.get(id=1)
		field_label = profile._meta.get_field('phone').verbose_name
		self.assertEquals(field_label, 'phone')

	def test_user_label(self):
		profile = UserProfile.objects.get(id=1)
		field_label = profile._meta.get_field('user').verbose_name
		self.assertEquals(field_label, 'user')

	def test_address_max_length(self):
		profile = UserProfile.objects.get(id=1)
		max_length = profile._meta.get_field('address').max_length
		self.assertEquals(max_length, 100)

	def test_phone_max_length(self):
		profile = UserProfile.objects.get(id=1)
		max_length = profile._meta.get_field('phone').max_length
		self.assertEquals(max_length, 15)

	def test_profile_first_name(self):
		profile = UserProfile.objects.get(id=1)
		first_name = profile.user.first_name
		self.assertEquals(first_name, 'Bob') 

	def test_profile_last_name(self):
		profile = UserProfile.objects.get(id=1)
		last_name = profile.user.last_name
		self.assertEquals(last_name, 'Test')

	def test_profile_email(self):
		profile = UserProfile.objects.get(id=1)
		email = profile.user.email
		self.assertEquals(email, 'bob@test.com')  

	def test_profile_phone(self):
		profile = UserProfile.objects.get(id=1)
		phone = profile.phone
		self.assertEquals(phone, '222-222-2222') 

	def test_profile_address(self):
		profile = UserProfile.objects.get(id=1)
		address = profile.address
		self.assertEquals(address, 'Test') 





"""
	def test_hours_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('hours').verbose_name
        self.assertEquals(field_label, 'hours')

    def test_wage_hour_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('wage_hour').verbose_name
        self.assertEquals(field_label, 'wage hour')

    def test_payment_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('payment').verbose_name
        self.assertEquals(field_label, 'payment')

    def test_is_temp_label(self):
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('is_temp').verbose_name
        self.assertEquals(field_label, 'is temp')

    def test_wage_hour_max_digits(self):
        employee = Employee.objects.get(id=1)
        max_digits = employee._meta.get_field('wage_hour').max_digits
        self.assertEquals(max_digits, 4)

    def test_hours_max_digits(self):
        employee = Employee.objects.get(id=1)
        max_digits = employee._meta.get_field('hours').max_digits
        self.assertEquals(max_digits, 10)
        """
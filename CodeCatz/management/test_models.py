from django.test import TestCase
#from django.auth import User
from .models import Employee
from register.models import *

class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user = User()
        test_user.save()
        test_profile = UserProfile.objects.get(id=test_user.id)
        Employee.objects.create(profile=test_profile)

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

    def test_payment_max_digits(self):
        employee = Employee.objects.get(id=1)
        max_digits = employee._meta.get_field('payment').max_digits
        self.assertEquals(max_digits, 10)

    def test_wage_hour_decimal_places(self):
        employee = Employee.objects.get(id=1)
        decimal_places = employee._meta.get_field('wage_hour').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_hours_decimal_places(self):
        employee = Employee.objects.get(id=1)
        decimal_places = employee._meta.get_field('hours').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_payment_decimal_places(self):
        employee = Employee.objects.get(id=1)
        decimal_places = employee._meta.get_field('payment').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_wage_hour_default(self):
        employee = Employee.objects.get(id=1)
        default = employee._meta.get_field('wage_hour').default
        self.assertEquals(default, 15.30)

    def test_is_temp_default(self):
        employee = Employee.objects.get(id=1)
        default = employee._meta.get_field('is_temp').default
        self.assertEquals(default, False)

    




"""
    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')
"""
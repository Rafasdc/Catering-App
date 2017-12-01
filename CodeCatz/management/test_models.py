from django.test import TestCase
from .models import Employee
from events.models import Event
from register.models import *

class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user = User()
        test_user.first_name = 'Bob'
        test_user.last_name = 'Test'
        test_user.email = 'bob@test.com'
        test_user.save()
        test_profile = UserProfile.objects.get(id=test_user.id)
        test_profile.phone='222-222-2222'
        test_profile.save()
        test_event = Event(user=test_user)
        test_event.numGuests = 200
        test_event.save()
        test_employee = Employee.objects.create(profile=test_profile)
        test_employee.event = (test_event,)
        test_employee.save()


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

    def test_employee_first_name(self):
        employee = Employee.objects.get(id=1)
        first_name = employee.profile.user.first_name
        self.assertEquals(first_name, 'Bob')

    def test_employee_last_name(self):
        employee = Employee.objects.get(id=1)
        last_name = employee.profile.user.last_name
        self.assertEquals(last_name, 'Test')

    def test_employee_email(self):
        employee = Employee.objects.get(id=1)
        email = employee.profile.user.email
        self.assertEquals(email, 'bob@test.com')

    def test_employee_phone(self):
        employee = Employee.objects.get(id=1)
        phone = employee.profile.phone
        self.assertEquals(phone, '222-222-2222')

    def test_employee_event(self):
        employee = Employee.objects.get(id=1)
        event = employee.event.first().id
        self.assertEquals(event,1)
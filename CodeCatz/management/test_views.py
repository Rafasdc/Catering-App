from django.test import TestCase
from .models import Employee
from events.models import Event
from register.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group

class DashboardView(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user_manager = User()
        test_user_manager.first_name = 'Bob'
        test_user_manager.last_name = 'Test'
        test_user_manager.username = 'bob'
        test_user_manager.set_password('12345')
        test_user_manager.email = 'bob@test.com'
        test_user_manager.save()
        employees, created = Group.objects.get_or_create(name='employees')
        managers, created = Group.objects.get_or_create(name='managers')
        g = Group.objects.get(name='managers') 
        g.user_set.add(test_user_manager)
        test_profile = UserProfile.objects.get(id=test_user_manager.id)
        test_profile.phone='222-222-2222'
        test_profile.save()
        test_event = Event(user=test_user_manager)
        test_event.numGuests = 200
        test_event.save()
        test_employee = Employee.objects.create(profile=test_profile)
        test_employee.event = (test_event,)
        test_employee.save()


    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/management/', follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accesible_by_name(self):
        resp = self.client.get(reverse('management:dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_no_manager(self):
        resp = self.client.get(reverse('management:dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'catering/index.html')

    def test_view_uses_correct_template_is_manager(self):
        login = self.client.login(username='bob', password='12345')
        resp = self.client.get(reverse('management:dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(str(resp.context['user']), 'bob')
        self.assertTemplateUsed(resp,'management/dashboard.html')


class EmployeeDashboardView(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User()
        test_user.first_name = 'Bob'
        test_user.last_name = 'Test'
        test_user.username = 'bob'
        test_user.set_password('12345')
        test_user.email = 'bob@test.com'
        test_user.save()
        employees, created = Group.objects.get_or_create(name='employees')
        g = Group.objects.get(name='employees') 
        g.user_set.add(test_user)
        test_profile = UserProfile.objects.get(id=test_user.id)
        test_profile.phone='222-222-2222'
        test_profile.save()
        test_event = Event(user=test_user)
        test_event.numGuests = 200
        test_event.save()
        test_employee = Employee.objects.create(profile=test_profile)
        test_employee.event = (test_event,)
        test_employee.save()

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/management/employee/', follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accesible_by_name_fail_no_employee(self):
        resp = self.client.get(reverse('management:employee_dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_fail_no_employee(self):
        resp = self.client.get(reverse('management:employee_dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'catering/index.html')

    def test_view_uses_correct_template_success_is_employee(self):
        login = self.client.login(username='bob', password='12345')
        resp = self.client.get(reverse('management:employee_dashboard'), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'management/employee_view.html')


class EmployeeView(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User()
        test_user.first_name = 'Bob'
        test_user.last_name = 'Test'
        test_user.username = 'bob'
        test_user.set_password('12345')
        test_user.email = 'bob@test.com'
        test_user.save()
        employees, created = Group.objects.get_or_create(name='employees')
        g = Group.objects.get(name='employees') 
        g.user_set.add(test_user)
        test_profile = UserProfile.objects.get(id=test_user.id)
        test_profile.phone='222-222-2222'
        test_profile.save()
        test_event = Event(user=test_user)
        test_event.numGuests = 200
        test_event.save()
        test_employee = Employee.objects.create(profile=test_profile)
        test_employee.event = (test_event,)
        test_employee.save()

    def test_view_url_exists_at_desired_location_not_logged_in(self):
        resp = self.client.get('/management/employee/1', follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accesible_by_name_fail_no_employee(self):
        resp = self.client.get(reverse('management:employee', kwargs={'employee_id' : 1}), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_fail_no_employee(self):
        resp = self.client.get(reverse('management:employee', kwargs={'employee_id' : 1}), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'catering/index.html')

    def test_view_url_accesible_by_name_success_is_employee(self):
        login = self.client.login(username='bob', password='12345')
        resp = self.client.get(reverse('management:employee', kwargs={'employee_id' : 1}), follow=True)
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template_success_is_employee(self):
        login = self.client.login(username='bob', password='12345')
        resp = self.client.get(reverse('management:employee', kwargs={'employee_id' : 1}), follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'management/employee_view.html')

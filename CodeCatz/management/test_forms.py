from django.test import TestCase

import datetime
from django.utils import timezone
from .forms import *
from events.models import Event

class EmployeeFormTest(TestCase):

    def test_employee_form_wage_field(self):
        form = EmployeeForm()
        self.assertTrue(form.fields['wage_hour'].label == None or form.fields['wage_hour'].label == 'Wage hour')

class AssignEmployeeEventFormTest(TestCase):
    
    def setUpTestData():
        #Set up non-modified objects used by all test methods
        test_user = User()
        test_user.first_name = 'Bob'
        test_user.last_name = 'Test'
        test_user.email = 'bob@test.com'
        test_user.save()
        test_profile = UserProfile.objects.get(id=test_user.id)
        test_profile.phone='222-222-2222'
        test_profile.save()
        test_event_1 = Event(user=test_user)
        test_event_1.numGuests = 200
        test_event_1.save()
        test_event_2 = Event(user=test_user)
        test_event_2.numGuests = 200
        test_event_2.save()
        test_employee = Employee.objects.create(profile=test_profile)
        test_employee.event = (test_event_1,test_event_2)
        test_employee.save()
    

    def test_assign_employee_event_form_event_field(self):
        form = AssignEmployeeEvent()
        self.assertTrue(form.fields['event'].label == None or form.fields['wage_hour'].label == 'Event')
    
    #Overlap on same date and same start time
    def test_assign_employee_event_form_event_overlap_full(self):
        test_event_1 = Event.objects.get(id=1)
        test_event_2 = Event.objects.get(id=2)
        event = (test_event_1, test_event_2)
        form_data = {'event':event}
        form = AssignEmployeeEvent(data=form_data)
        self.assertFalse(form.is_valid())

    #Overlap on running time (same date, but different start times)
    def test_assign_employee_event_form_event_overlap_hours(self):
        test_event_1 = Event.objects.get(id=1)
        test_event_1.startTime = datetime.time(12,00)
        test_event_1.save()
        test_event_2 = Event.objects.get(id=2)
        event = (test_event_1, test_event_2)
        form_data = {'event':event}
        form = AssignEmployeeEvent(data=form_data)
        self.assertFalse(form.is_valid())

    #No overlaping between events
    def test_assign_employee_event_form_event_no_overlap(self):
        test_event_1 = Event.objects.get(id=1)
        test_user = User.objects.get(id=1)
        test_event_1.date = test_event_1.date + datetime.timedelta(days=7)
        test_event_1.save()
        print(test_event_1.date)
        test_event_2 = Event.objects.get(id=2)
        event = (test_event_1, test_event_2)
        form_data = {'event':event}
        form = AssignEmployeeEvent(data=form_data)
        self.assertTrue(form.is_valid())
    


    """
    def test_renew_form_date_field_label(self):
        form = RenewBookForm()        
        self.assertTrue(form.fields['renewal_date'].label == None or form.fields['renewal_date'].label == 'renewal date')

    def test_renew_form_date_field_help_text(self):
        form = RenewBookForm()
        self.assertEqual(form.fields['renewal_date'].help_text,'Enter a date between now and 4 weeks (default 3).')

    def test_renew_form_date_in_past(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_too_far_in_future(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_renew_form_date_today(self):
        date = datetime.date.today()
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_renew_form_date_max(self):
        date = timezone.now() + datetime.timedelta(weeks=4)
        form_data = {'renewal_date': date}
        form = RenewBookForm(data=form_data)
        self.assertTrue(form.is_valid())
    """
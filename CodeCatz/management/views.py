from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from .models import *
from events.models import Event
from .forms import *
from events.models import *
from register.forms import *
import sys

def is_manager(user):
	return user.groups.filter(name='managers').exists()

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def dashboard(request):
	employee_list = Employee.objects.all()
	event_list = Event.objects.all()
	context = {'employee_list': employee_list, 'event_list': event_list}
	return render(request, 'management/dashboard.html', context)

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def view_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	employee.calculate_hours_worked()
	employee.calculate_payment()
	events = employee.event.all()
	context = {'employee' : employee, 'events': events}
	return render (request, 'management/employee_view.html', context)

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def assign_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	events_list = Event.objects.all()
	employee_events = employee.event.all()
	events = []
	for event in employee_events:
		events.append(event.id)
	formset = AssignEmployeeEvent(request.POST or None, initial={'event': events});
	if request.method == 'POST':
		if formset.is_valid():
			to_assign = formset.cleaned_data.get('event')
			#print (validate_dates(to_assign))
			employee.event = formset.cleaned_data.get('event')
			employee.save()
			return HttpResponseRedirect(reverse('management:employee', kwargs={'employee_id': employee_id}))
		else:
			print(formset.errors)
	context = {'employee': employee,'formset': formset, 'events_list': events_list}
	return render(request, 'management/employee_assign.html', context)

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def create_employee(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)   
        profile_form = ProfileForm(request.POST)
        g = Group.objects.get(name='employees') 
        if form.is_valid() and profile_form.is_valid():
            created_user = form.save()
            g.user_set.add(created_user)
            created_profile = UserProfile.objects.get(id=created_user.pk)
            created_profile.phone = profile_form.cleaned_data.get('phone')
            created_profile.address = profile_form.cleaned_data.get('address')
            created_profile.save()
            created_employee = Employee()
            created_employee.profile = created_profile            
            created_employee.save()
            return redirect(reverse('management:dashboard'))         
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'register/signup.html', {
            "form": form,
            "profile_form": profile_form,
        })

@user_passes_test(is_manager)
def payment_event(request):
	"""
	Event Payment
	"""
	event_list = Event.objects.all()
	for event in event_list:
		event.calculate_menu_cost()
		event.calculate_employee_cost()
		event.calculate_suggested_price()
	context = {'event_list' : event_list}
	return render(request, 'management/event_payment.html', context)

	



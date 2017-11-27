from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .forms import *
from events.models import *
from register.forms import *
import sys

def is_manager(user):
	return user.groups.filter(name='managers').exists()
"""
def validate_dates(events):
	for event1 in events:
		for event2 in events:
			print(event1.id)
			print(event2.id)
			#print(vars(event2))
			if (event1.date == event2.date) and (event1.id != event2.id):
				print(event1.startTime)
				print(event2.startTime)
				#events start at the same time
				if (event1.startTime == event2.startTime):
					return False
					#raise Exception ("Event %s and %s overlap." (event1, event2))
				#overlap in range
				if (event1.startTime < event2.startTime) and (event1.endTime >= event2.endTime):
					#raise Exception ("Event %s and %s overlap." (event1, event2))
					return False
	return True
"""
@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def dashboard(request):
	employee_list = Employee.objects.all()
	event_list = Event.objects.all()
	context = {'employee_list': employee_list, 'event_list': event_list}
	return render(request, 'management/dashboard.html', context)

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def view_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	events = employee.event.all()
	context = {'employee' : employee, 'events': events}
	return render (request, 'management/employee_view.html', context)

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def assign_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	employee_events = employee.event.all()
	events = []
	for event in employee_events:
		events.append(event.id)
	#print(employee_events)
	form = AssignEmployeeEvent(request.POST or None, initial={'event': events});
	context = {'employee': employee,'form': form}
	if request.method == 'POST':
		if form.is_valid():
			to_assign = form.cleaned_data.get('event')
			#print (validate_dates(to_assign))
			employee.event = form.cleaned_data.get('event')
			employee.save()
			return HttpResponseRedirect(reverse('management:employee', kwargs={'employee_id': employee_id}))
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
        	print("invalid form")
        	print(form.errors)          
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'register/signup.html', {
            "form": form,
            "profile_form": profile_form,
        })

@user_passes_test(is_manager)
def edit_employee(request, employee_id):
	"""
	Edit employee
	"""


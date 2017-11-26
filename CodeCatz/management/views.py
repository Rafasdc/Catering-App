from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *
from events.models import *
from register.forms import *

def dashboard(request):
	employee_list = Employee.objects.all()
	event_list = Event.objects.all()
	context = {'employee_list': employee_list, 'event_list': event_list}
	return render(request, 'management/dashboard.html', context)

def view_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	events = employee.event.all()
	context = {'employee' : employee, 'events': events}
	return render (request, 'management/employee_view.html', context)

def assign_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	events = []
	for event in employee.event.all():
		events.append(event.eventID)
	form = AssignEmployeeEvent(request.POST or None, initial={'event': events});
	context = {'employee': employee,'form': form}
	if request.method == 'POST':
		if form.is_valid():
			employee.event = form.cleaned_data.get('event')
			employee.save()

			return HttpResponseRedirect(reverse('management:employee', kwargs={'employee_id': employee_id}))
	return render(request, 'management/employee_assign.html', context)

def create_employee(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)   
        profile_form = ProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            created_user = form.save()
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

def edit_employee(request, employee_id):
	"""
	Edit employee
	"""


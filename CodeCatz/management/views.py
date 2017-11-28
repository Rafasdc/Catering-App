from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from .models import *
from events.models import Event
from register.models import *
from .forms import *
from .services import *
from events.models import *
from register.forms import *
import random

def is_manager(user):
	return user.groups.filter(name='managers').exists()

def is_employee(user):
	return (user.groups.filter(name='employees').exists())

def is_manager_or_employee(user):
	return (user.groups.filter(name='employees').exists()) or (user.groups.filter(name='managers').exists())

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def dashboard(request):
	employee_list = Employee.objects.all()
	event_list = Event.objects.all()
	context = {'employee_list': employee_list, 'event_list': event_list}
	return render(request, 'management/dashboard.html', context)

@user_passes_test(is_employee, redirect_field_name = '/', login_url='/')
def employee_dashboard(request):
	print (request.user.id)
	print (Employee.objects.get(profile_id=request.user.id))
	employee_id = Employee.objects.get(profile_id=request.user.id).id
	return HttpResponseRedirect(reverse('management:employee', kwargs={'employee_id':employee_id}))

@user_passes_test(is_manager_or_employee, redirect_field_name = '/', login_url='/')
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

@user_passes_test(is_manager, redirect_field_name = '/', login_url='/')
def edit_wage(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	if request.method =='POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			employee = Employee.objects.get(id=employee_id)
			employee.wage_hour = form.cleaned_data.get('wage_hour')
			employee.save()
			return redirect(reverse('management:employee', kwargs={'employee_id': employee_id}))
	else:
		form = EmployeeForm()
	context = {'form': form}
	return render(request, 'management/wage_edit.html', context)

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

@user_passes_test(is_manager)
def hire_temp_employee(request):
		temp = get_temp_employee()
		temp_user = User()
		temp_user.first_name = (temp[0]['name']['first']).title()
		temp_user.last_name = temp[0]['name']['last'].title()
		temp_user.username = temp[0]['login']['username']
		temp_user.password = 'catz1234'
		temp_user.email = temp[0]['email']
		temp_profile = UserProfile(user=temp_user)
		print(temp[0]['phone'])
		temp_profile.phone = temp[0]['phone']
		temp_employee = Employee(profile=temp_profile)
		temp_employee.is_temp = True
		temp_employee.wage_hour = round(random.uniform(10,20),2)
		g = Group.objects.get(name='employees') 
		temp_user.save()
		g.user_set.add(temp_user)
		created_profile = UserProfile.objects.get(id=temp_user.pk)
		created_profile.phone = temp_profile.phone
		created_profile.save()
		temp_employee.profile = created_profile
		temp_employee.save()
		context = {'temp_employee': temp_employee}
		return render(request, 'management/temp_employee.html', context)



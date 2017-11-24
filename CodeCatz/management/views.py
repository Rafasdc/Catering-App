from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

def dashboard(request):
	employee_list = Employee.objects.all()
	context = {'employee_list': employee_list}
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

def edit_employee(request, employee_id):
	"""
	Edit employee
	"""


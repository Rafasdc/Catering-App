from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def dashboard(request):
	employee_list = Employee.objects.all()
	context = {'employee_list': employee_list}
	return render(request, 'management/dashboard.html', context)

def manage_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	roles = Role.objects.all()
	form = AssignEmployee(request.POST);
	context = {'employee': employee, 'roles': roles, 'form': form}
	if request.method == 'POST':
		if form.is_valid():
			employee.role = form.cleaned_data.get('role')
			employee.save()
	return render(request, 'management/employee.html', context)


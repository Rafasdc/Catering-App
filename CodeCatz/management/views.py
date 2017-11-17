from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def dashboard(request):
	employee_list = Employee.objects.all()
	context = {'employee_list': employee_list}
	return render(request, 'management/dashboard.html', context)

def manage_employee(request, employee_id):
	employee = Employee.objects.get(id=employee_id)
	roles = Role.objects.all()
	context = {'employee': employee, 'roles': roles}
	return render(request, 'management/employee.html', context)


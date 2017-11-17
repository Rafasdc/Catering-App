from django.shortcuts import render
from .models import Employee

def dashboard(request):
	employee_list = Employee.objects.all()
	context = {'employee_list': employee_list}
	return render(request, 'management/dashboard.html', context)

# Create your views here.

from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'management'
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^employee/$', views.employee_dashboard, name='employee_dashboard'),
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.view_employee, name='employee'),
    url(r'^employee/(?P<employee_id>[0-9]+)/events/$', views.assign_employee, name='employee_assign'),
    url(r'^employee/create/$', views.create_employee, name='create_employee'),
    url(r'^employee/wage/(?P<employee_id>[0-9]+)/$', views.edit_wage, name='edit_wage'),
    url(r'^events/payment/$', views.payment_event, name='event_price'),
    url(r'^employee/temp/$', views.hire_temp_employee, name='temp_employee'),



]
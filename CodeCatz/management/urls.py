from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'management'
urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^employee/(?P<employee_id>[0-9]+)/$', views.view_employee, name='employee'),
    url(r'^employee/(?P<employee_id>[0-9]+)/events/$', views.assign_employee, name='employee_assign'),
    url(r'^employee/(?P<employee_id>[0-9]+)/edit/$', views.edit_employee, name='employee_edit'),
    url(r'^employee/create/$', views.create_employee, name='create_employee'),
]
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^employee/(?P<employee_id>[0-9]+)/', views.manage_employee, name='employee'),

]
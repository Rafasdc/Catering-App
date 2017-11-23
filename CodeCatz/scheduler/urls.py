from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
		url(r'^email/$', views.email, name='email'),
		url(r'^success/$', views.success, name='success'),
]
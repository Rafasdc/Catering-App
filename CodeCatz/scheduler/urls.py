from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
		url(r'^email/$', views.EmailView.as_view(), name='email'),
		url(r'^thanks/$', views.EmailView.as_view(), name='thanks'),
]
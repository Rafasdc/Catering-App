from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
		url(r'^contact/$', views.EmailView.as_view(), name='contact'),
		url(r'^success/$', TemplateView.as_view(template_name="scheduler/success.html"), name='contact-success'),
]
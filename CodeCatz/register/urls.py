from django.conf.urls import url
from django.views.generic import TemplateView

from register.views import signup as register_signup


urlpatterns = [
    url(r'^signup/$', register_signup, name='register'),
]
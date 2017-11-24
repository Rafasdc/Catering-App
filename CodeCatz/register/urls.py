from django.conf.urls import url
from django.views.generic import TemplateView

from register.views import *


urlpatterns = [
    url(r'^signup/$', signup, name='register'),
    url(r'^account/(?P<pk>[\-\w]+)/$', edit_user, name='edit'),

]
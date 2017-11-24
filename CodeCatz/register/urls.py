from django.conf.urls import url
from django.views.generic import TemplateView

from register.views import *


urlpatterns = [
    url(r'^signup/$', signup, name='register'),
    url(r'^account/(?P<pk>[\-\w]+)/$', view_user, name='view_account'),
    url(r'^account/edit/(?P<pk>[\-\w]+)/$', edit_user, name='edit_account'),

]
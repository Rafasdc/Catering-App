from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.EventDetailView.as_view(), name='events'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create-event'),
    url(r'^update/(?P<pk>\d+)/$', views.EventEditView.as_view(), name='event-update'),
]
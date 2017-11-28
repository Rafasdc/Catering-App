from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.EventDetailView.as_view(), name='events'),
    url(r'^create/$', views.EventCreateView.as_view(), name='create-event'),
    url(r'^update/(?P<pk>\d+)/$', views.EventEditView.as_view(), name='event-update'),
    url(r'^manager_update/(?P<pk>\d+)/$', views.ManagerEditView.as_view(), name='manager-event-update'),
    url(r'^manager_delete/(?P<pk>\d+)/$', views.ManagerDeleteView.as_view(), name='manager-event-delete'),
    url(r'^cancel/(?P<pk>\d+)/$', views.UserDeleteView.as_view(), name='event-delete'),

]
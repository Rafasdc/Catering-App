from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^event_detail/', TemplateView.as_view(template_name="events/event_detail.html"), name='book'),
]
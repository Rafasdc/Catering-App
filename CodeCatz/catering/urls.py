from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="catering/index.html"), name='home'),
    url(r'^schedule/$',views.schedule, name='schedule'),

    url(r'^database/$',views.database)
   
]
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class EventDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['events'] =  Event.objects.filter(user=self.request.user)
        return context

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class EventDetailView(LoginRequiredMixin,generic.DetailView):
    model = Event
    context_object_name = 'event_detail'
    template_name = 'events/event_detail.html'

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).filter(status__exact='o').order_by('date')
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView, UpdateView
from .forms import CreateEventForm
from django.urls import reverse_lazy

class EventDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'events/events.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['events'] =  Event.objects.filter(user=self.request.user)
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    """
    Create an event
    """
    model = Event
    form_class = CreateEventForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(EventCreateView, self).form_valid(form)

    def get_queryset(self):
        return Event.objects.filter(user=self.request.user).order_by('date')

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('events')


class EventEditView(LoginRequiredMixin, UpdateView):
    """
    Update an event
    """
    model = Event
    fields = ['event_type', 'numGuests', 'date', 'startTime', 'endDate', 'endTime', 'location', 'menu']

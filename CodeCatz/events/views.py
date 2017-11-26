from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView, UpdateView
from .forms import CreateEventForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

class OwnershipMixin(object):
    """
    Mixin providing a dispatch overload that checks object ownership. is_staff and is_supervisor
    are considered object owners as well. This mixin must be loaded before any class based views
    are loaded for example class SomeView(OwnershipMixin, ListView)
    """
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        # we need to manually "wake up" self.request.user which is still a SimpleLazyObject at this point
        # and manually obtain this object's owner information.
        current_user = self.request.user
        object_owner = getattr(self.get_object(), 'user')
            
        if current_user.id != object_owner.id and not current_user.groups.filter(name='managers').exists(): 
            """and not current_user.is_superuser and not current_user.is_staff:"""
            raise PermissionDenied
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)

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


class EventEditView(OwnershipMixin, LoginRequiredMixin, UpdateView):
    """
    Update an event
    """

    model = Event
    fields = ['event_type', 'numGuests', 'date', 'startTime', 'endDate', 'endTime', 'location', 'menu', 'status']





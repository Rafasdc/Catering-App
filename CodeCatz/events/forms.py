from django import forms
from .models import Event
from scheduler.models import ScheduleManager

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['status', 'user']

    def save(self, user=None):
        event = super(CreateEventForm, self).save(commit=False)
        if user:
            event.user = user
        ScheduleManager.update(event)
        event.save()
        return event


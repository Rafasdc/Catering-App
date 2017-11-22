from django import forms
from .models import Event

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['status', 'user']
    
    def save(self, user=None):
        event = super(CreateEventForm, self).save(commit=False)
        if user:
            event.user = user
        event.save()
        return event
        

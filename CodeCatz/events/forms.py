from django import forms
from .models import Event
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['status', 'user', 'menu_cost', 'employee_cost', 'suggested_price']

    def clean(self):
        cleaned_data = super(CreateEventForm, self).clean()
        numGuests = cleaned_data.get('numGuests')
        date = cleaned_data.get('date')
        endDate = cleaned_data.get('endDate')
        startTime = cleaned_data.get('startTime')
        endTime = cleaned_data.get('endTime')

        if numGuests:
            if numGuests <= 0:
                self.add_error('numGuests', ValidationError(_("Guests can not be zero or less. ")))
        else:
            self.add_error('numGuests', ValidationError(_("Guests can not be zero or blank.")))

        if date and endDate:
            #Check date is not in past.
            if date < (datetime.date.today() + datetime.timedelta(days=7)):
                self.add_error('date', ValidationError(_('Invalid date - cannot create event sooner than 1 week in advance.')))

            #Check date is in range librarian allowed to change (+4 weeks).
            if date < datetime.date.today():
                self.add_error('date', ValidationError(_('Invalid date - in the past.')))

            if endDate < date:
                self.add_error('endDate', ValidationError(_("End date can not be before start date.")))
            if endDate == date:
                if( endTime < startTime):
                    self.add_error('endTime', ValidationError(_("End time cannot be before start time if on same day.")))
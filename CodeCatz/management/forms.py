from django import forms
from .models import *
from events.models import Event
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['wage_hour']

class AssignEmployeeEvent(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('event',)

	event = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), required=False, widget=CheckboxSelectMultiple)

	def clean_event(self):
		events = self.cleaned_data['event']
		for event1 in events:
			for event2 in events:
				#same date
				if (event1.date == event2.date) and (event1.id != event2.id):
					#events start at the same time
					if (event1.startTime == event2.startTime):
						raise ValidationError(_('Error: The events: %(event1)s and %(event2)s overelap.'), params={'event1': event1, 'event2': event2},)
					#overlap in range
					if (event1.startTime < event2.startTime) and (event1.endTime >= event2.endTime):
						raise ValidationError(_('Error: The events: %(event1)s and %(event2)s overelap.'), params={'event1': event1, 'event2': event2},)
		return events

	def save(self, commit=True):
		instance = forms.ModelForm.save(self, False)

		def save_m2m():
			old_save_m2m()
			instance.event_set.clear()
			for event in self.cleaned_data['event']:
				instance.event_set.add(event)
		self.save_m2m = save_m2m

		if commit:
			instance.save()
			self.save_m2m()

		return instance

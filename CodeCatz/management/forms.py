from django import forms
from .models import *
from events.models import Event
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['profile']

class AssignEmployeeEvent(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('event',)

	event = forms.ModelMultipleChoiceField(queryset=Event.objects.all(), required=False, widget=CheckboxSelectMultiple)

	def clean_event(self):
		events = self.cleaned_data['event']
		print(events)
		for event1 in events:
			for event2 in events:
				print(event1.id)
				print(event2.id)
				#print(vars(event2))
				if (event1.date == event2.date) and (event1.id != event2.id):
					print(event1.startTime)
					print(event2.startTime)
					#events start at the same time
					if (event1.startTime == event2.startTime):
						#return False
						raise ValidationError("Email already exists")
						#raise Exception ("Event %s and %s overlap." (event1, event2))
					#overlap in range
					if (event1.startTime < event2.startTime) and (event1.endTime >= event2.endTime):
						#raise Exception ("Event %s and %s overlap." (event1, event2))
						raise ValidationError("Email already exists")
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

class AssignEmployeeEventRole(forms.ModelForm):
	class Meta:
		model = Employee
		fields = ('role',)

	role = forms.ModelMultipleChoiceField(queryset=Role.objects.all())

	def __init__(self, *args, **kwargs):
		if kwargs.get('insance'):
			initial = kwargs.setdefault('initial', {})
			initial['role'] = [t.pk for t in kwargs['instance'].role_set.all()]
		forms.ModelForm.__init__(self, *args, **kwargs)

	def save(self, commit=True):
		instance = forms.ModelForm.save(self, False)

		def save_m2m():
			old_save_m2m()
			instance.role_set.clear()
			for role in self.cleaned_data['role']:
				instance.role_set.add(role)
		self.save_m2m = save_m2m

		if commit:
			instance.save()
			self.save_m2m()

		return instance
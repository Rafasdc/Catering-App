from django import forms
from .models import *

class AssignEmployee(forms.Form):
	role = forms.MultipleChoiceField(choices=Role.ROLE_CHOICES)


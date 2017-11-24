from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from .forms import EmailForm
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.conf import settings


def email(request):
	if request.method == 'GET':
		form = EmailForm()
	else:
		form = EmailForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['jasonsanche@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	return render(request, "scheduler/email.html", {'form': form})

def success(request):
	return HttpResponse('Success! Thank you for your message.')
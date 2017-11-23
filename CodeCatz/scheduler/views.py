from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from .forms import EmailForm
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

class EmailView(TemplateView):
	template_name = 'scheduler/email.html'

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
				return redirect('thanks')
			return render(request, "scheduler/email.html", {'form': form})

		def thanks(request):
			return HttpResponse('Thank you for your message.')
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import *
from .forms import EmailForm
from django.core import mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class EmailView(FormView):
	"""
	output a form
	"""
	form_class = EmailForm
	template_name = "scheduler/email.html"
	success_url = reverse_lazy("contact-success")

	def get_initial(self):
		"""
		Returns the initial data to use for forms on this view.
		"""
		initial = super(EmailView, self).get_initial()
		if(self.request.user.is_authenticated):
			initial['from_email'] = self.request.user.email

		return initial

	def form_valid(self, form):
		subject = form.cleaned_data['subject']
		from_email = form.cleaned_data['from_email']
		message = form.cleaned_data['message']
		try:
			mail.send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER,], fail_silently=False)
			return HttpResponseRedirect(self.get_success_url())
		except mail.BadHeaderError:
			return HttpResponse('Invalid header found.')


class ScheduleView(LoginRequiredMixin,ListView):
    #permission_required = 'catalog.can_mark_returned'
    model = Event
    template_name = 'scheduler/events.html'
    paginate_by = 10

    def get_queryset(self):
        return Event.objects.all().order_by('date')


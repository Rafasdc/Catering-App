from django.db import models
from django.urls import reverse
from events.models import Event
from django.contrib.auth.models import User
import datetime
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

class Notify(models.Model):
	"""
	notifies through email the necessary staff
	"""

	def sendEmail(emailto):
		from_email = settings.DEFAULT_FROM_EMAIL
		subject = 'Some subject'
		recipient_list = settings.LIST_OF_EMAIL_RECIPIENTS
		message = settings.EMAIL_MESSAGE(default = 'Pending')
		html_message = '<h1>This is my HTML test</h1>'
		send_mail(subject, message, from_email, emailto,fail_silently=False, html_message=html_message)


	def __str__(self):
		return self.name


class ScheduleManager(models.Model):
	"""
	manages the logic for tagging and notifications
	"""






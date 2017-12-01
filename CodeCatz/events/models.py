from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.db.models import signals
from django.core.mail import send_mail
from django.dispatch import receiver
import datetime
import management
import decimal
from menu.models import Menu
from django.utils.translation import ugettext_lazy as _


def default_start_day():
    	return datetime.datetime.today() + datetime.timedelta(days=7)


# For event
class Event(models.Model):

	EVENT_TYPE = (
		('Wedding', 'Wedding'),
		('Corporate', 'Corporate'),
		('Private', 'Private'),
		('Social', 'Social'),
		('Bar', 'Bar'),
	)

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event_type = models.CharField(
	    max_length=50, choices=EVENT_TYPE, blank=True, default='Social', help_text='Event type.')
	numGuests = models.IntegerField(
	    'Number of Guests', help_text="Enter the number of guests.")
	date = models.DateField(default=default_start_day,
	                        help_text="Enter date of event.")
	startTime = models.TimeField(default=datetime.time(
	    16, 00), help_text="Specify start time of event.")
	endDate = models.DateField(default=default_start_day,
	                           help_text="If event goes into next day, please edit.")
	endTime = models.TimeField(default=datetime.time(
	    22, 00), help_text="Enter end time.")
	location = models.CharField(max_length=255, help_text="Enter location")
	menu = models.ForeignKey(Menu, null=True, blank=True,
	                         help_text="Choose a menu")
	menu_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	employee_cost = models.DecimalField(
	    max_digits=6, decimal_places=2, default=0.00)
	suggested_price = models.DecimalField(
	    max_digits=10, decimal_places=2, default=0.00)

	EVENT_STATUS = (
		('p', 'Pending'),
		('a', 'Approved'),
		('n', 'Notified'),
		('w', 'Working On'),
		('c', 'Complete'),
	)

	status = models.CharField(max_length=1, choices=EVENT_STATUS, blank=True, default='p',
		help_text='Event Status')

	def __str__(self):
		return "%s, %s guests" % (self.user, self.numGuests)

	def get_absolute_url(self):
		return reverse('events')

	class Meta:
		ordering = ["date"]
		permissions = (("can_mark_approved", "Set event as approved."),)

	@property
	def getEndDate(self):
		return self.endDate

	def calculate_menu_cost(self):
		total_cost = 0
		print(self.menu)
		for menu_items in self.menu.menu_items.all():
			for recipe in menu_items.menu_constituents.all():
				total_cost += recipe.cost
		self.menu_cost = round(total_cost, 2)
		self.save()

	def calculate_employee_cost(self):
		total_cost = 0
		employee_list = management.models.Employee.objects.all()
		for employee in employee_list:
			for employee_events in employee.event.all():
				if employee_events.id == self.id:
					time_start = datetime.datetime.combine(self.date, self.startTime)
					time_end = datetime.datetime.combine(self.endDate, self.endTime)
					hours_worked = time_end - time_start
					hours_worked_dec = hours_worked.total_seconds() / 3600
					employee_cost = employee.wage_hour * decimal.Decimal(hours_worked_dec)
					total_cost += employee_cost
		self.employee_cost = round(total_cost, 2)
		self.save()

	def calculate_suggested_price(self):
		total_cost = self.menu_cost + self.employee_cost
		# 30% profit
		suggested_price = total_cost * decimal.Decimal(1.30)
		self.suggested_price = round(suggested_price, 2)
		self.save()





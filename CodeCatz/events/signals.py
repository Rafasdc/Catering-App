from django.db.models import signals
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Event
from django.conf import settings
import datetime

@receiver(signals.post_save, sender=Event)
def event_post_save(sender, instance, signal, *args, **kwargs):

	if instance.status == "p":
		#send to manager
		send_mail('Event {:d} is pending.'.format(instance.id), "There is a pending event from {:s} {:s}. Please confirm the details on the management tab.".format(instance.user.first_name, instance.user.last_name), "automated@code.catz.ca", [settings.EMAIL_HOST_USER,], fail_silently=False)
	if instance.status == "a":
    	#send to user
		endDate = instance.getEndDate
		endTime = instance.endTime
		compare = datetime.datetime.combine(endDate, endTime)
		send_mail('Event Approved!', "Hi {:s} {:s}, \n\n This is to notify you that your event on {:%B %d, %Y} has been approved. We will email you one week beforehand to confirm. \n\n Thanks,\nCats Catering".format(instance.user.first_name, instance.user.last_name, compare), "automated@code.catz.ca", [instance.user.email], fail_silently=False)

from django.db.models import signals
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Event
from django.conf import settings

@receiver(signals.post_save, sender=Event)
def event_post_save(sender, instance, signal, *args, **kwargs):
	if instance.status == "p":    
		send_mail('New event request (CodeCatz)', "There is a new event. Please confirm the details on the management tab.", "automated@code.catz.ca", [settings.EMAIL_HOST_USER,], fail_silently=False)


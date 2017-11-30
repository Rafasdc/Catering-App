from django.apps import AppConfig
import datetime
from django.db.models import signals
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings


class SchedulerConfig(AppConfig):
    name = 'scheduler'
    verbose_name = "Scheduler"
    def ready(self):
        from events.models import Event

        events = Event.objects.all()
        for event in events:
            endDate = event.getEndDate
            endTime = event.endTime
            compareEnd = datetime.datetime.combine(endDate, endTime)
            date = event.date
            startTime = event.startTime
            compareStart = datetime.datetime.combine(date, startTime)
            now = datetime.datetime.now()

            if(compareEnd < now):
                if event.status != 'c':
                    user = event.user
                    userEmail = user.email
                    send_mail('Event Over, Please Delete', "Event {:d} from {:%B %d, %Y} by user {:s} {:s} is over. Please confirm payment and delete.".format(event.id, compareEnd, user.first_name, user.last_name), "automated@code.catz.ca", [settings.EMAIL_HOST_USER,], fail_silently=False)
                    event.status = 'c'
                    event.save()

            elif(now > (compareStart-datetime.timedelta(weeks=1))):
                user = event.user
                if(event.status == 'p'):
                    send_mail('One week before event {:d}, still pending'.format(event.id), "There is a pending event from {:s} {:s} and their event starts on {:%B %d, %Y}. Please confirm the details on the management tab.".format(user.first_name, user.last_name, compareStart), "automated@code.catz.ca", [settings.EMAIL_HOST_USER,], fail_silently=False)
                elif(event.status == 'a'):
                    #For manager
                    send_mail('One week before event {:d}'.format(event.id), "There is an event from {:s} {:s} and their event starts on {:%B %d, %Y}. Please confirm employees and inventory for the event.".format(user.first_name, user.last_name, compareStart), "automated@code.catz.ca", [settings.EMAIL_HOST_USER,], fail_silently=False)
                    #For user
                    send_mail('One Week Before Your Event!', "Hi {:s} {:s},\n\n This is to notify you that your event on {:%B %d, %Y} is well on its way! Please email back to confirm.\n\nWe will see you soon,\n Cats Catering".format(user.first_name, user.last_name,compareStart), "automated@code.catz.ca", [user.email], fail_silently=False)
                    event.status = 'n'
                    event.save()

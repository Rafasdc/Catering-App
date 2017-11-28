from django.db import models
from django.urls import reverse
from events.models import Event
from django.contrib.auth.models import User
import datetime
from django.core import mail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings




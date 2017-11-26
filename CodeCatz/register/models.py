from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

class Person(models.Model):
    """
    Model for all employees and customers
    """
    address = models.TextField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(help_text="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",validators=[phone_regex], max_length=15, null=True, blank=False) # validators should be a list

    class Meta:
        abstract = True

class UserProfile(Person):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()
    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return self.user.__str__()


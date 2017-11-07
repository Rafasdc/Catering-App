from django.core.management.base import BaseCommand

#Put commands in class Command(BaseCommand) to populate database
"""Example, created using Models from Mozilla Developers code, and seperate function from 
https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database

from catalog.models import Author, Genre, Language, Book, BookInstance
import datetime
class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_authors(self):
        afirst, created = Author.objects.get_or_create(first_name='first', last_name = 'second', date_of_birth= datetime.datetime(1994, 6, 17))
        afirst.save()

        asecond, created = Author.objects.get_or_create(first_name='Jar', last_name = 'Jar', date_of_birth= datetime.datetime(1964, 12, 7))
        asecond.save()

    def handle(self, *args, **options):
        self._create_authors()

"""


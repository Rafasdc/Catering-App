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
from menu.models import Category, Ingredient


class Command(BaseCommand):
    def _create_food_database(self):
        """
        Categories
        """
        p, created = Category.objects.get_or_create(title="Proteins")
        p.save()
        d, created = Category.objects.get_or_create(title="Dairy")
        d.save()
        fo, created = Category.objects.get_or_create(title="Fats and Oils")
        fo.save()
        s, created = Category.objects.get_or_create(title="Seasoning")
        s.save()
        c, created = Category.objects.get_or_create(title="Condiments")
        c.save()
        v, created = Category.objects.get_or_create(title="Vegetables")
        v.save()
        f, created = Category.objects.get_or_create(title="Fruits")
        f.save()
        b, created = Category.objects.get_or_create(title="Baking")
        b.save()
        bf, created = Category.objects.get_or_create(title="Breakfast")
        bf.save()
        g, created = Category.objects.get_or_create(title="Grains")
        g.save()
        ns, created = Category.objects.get_or_create(title="Nuts and Seeds")
        ns.save()
        carb, created = Category.objects.get_or_create(title="Carbohydrates")
        carb.save()
        ss, created = Category.objects.get_or_create(title="Sugar and Spices")
        ss.save()

        """
        Ingredients
        """
        white_sugar, created = Ingredient.objects.get_or_create(name="White Sugar", category=ss)
        white_sugar.save()
        butter, created = Ingredient.objects.get_or_create(name="Butter", category=fo)
        butter.save()
        eggs, created = Ingredient.objects.get_or_create(name="Eggs", category=p)
        eggs.save()
        vanilla_extract, created = Ingredient.objects.get_or_create(name="Vanilla Extract", category=b)
        vanilla_extract.save()
        flour, created = Ingredient.objects.get_or_create(name="Flour", category=b)
        flour.save()
        baking_powder, created = Ingredient.objects.get_or_create(name="Baking Powder", category=b)
        baking_powder.save()
        milk, created = Ingredient.objects.get_or_create(name="Milk", category=d)
        milk.save()
        steak, created = Ingredient.objects.get_or_create(name="Steak", category=p)
        steak.save()
        olive_oil, created = Ingredient.objects.get_or_create(name="Olive Oil", category=fo)
        olive_oil.save()
        salt, created = Ingredient.objects.get_or_create(name="Salt", category=s)
        salt.save()
        black_pepper, created = Ingredient.objects.get_or_create(name="Black Pepper", category=s)
        black_pepper.save()
        

        """
        Add your own recipes and quantities on /admin/, easier. Populate ingredients here.
        """


    def handle(self, *args, **options):
        self._create_food_database()


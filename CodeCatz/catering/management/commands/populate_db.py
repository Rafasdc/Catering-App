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
        romaine_lettuce, created = Ingredient.objects.get_or_create(name="Romaine Lettuce", category=v)
        romaine_lettuce.save()
        roma_tomato, created = Ingredient.objects.get_or_create(name="Roma Tomato", category=v)
        roma_tomato.save()
        carrot, created = Ingredient.objects.get_or_create(name="Carrot", category=v)
        carrot.save()
        red_cabbage, created = Ingredient.objects.get_or_create(name="Red Cabbage", category=v)
        red_cabbage.save()
        self.create_ingredient("Cucumber", v)
        self.create_ingredient("Red Onion", v)
        self.create_ingredient("Cheddar Cheese", d)
        self.create_ingredient("Ranch", c)
        self.create_ingredient("Potato", v)
        self.create_ingredient("Sour Cream", d)
        self.create_ingredient("Bacon", p)
        self.create_ingredient("Green Onion", v)
        self.create_ingredient("Ketchup", c) 
        self.create_ingredient("Apple", f)  
        self.create_ingredient("Chicken", p)    
        self.create_ingredient("Salmon", p)
        self.create_ingredient("Lemon", f)
        self.create_ingredient("Dill", ss)  
        self.create_ingredient("Rye Bread", carb)
        self.create_ingredient("Turkey Breast", p)


        """
        Add your own recipes and quantities on /admin/, easier. Populate ingredients here.
        """
    def create_category(self, name):
        temp, created = Category.objects.get_or_create(title=name)
        temp.save()
    
    def create_ingredient(self, name, category):
        temp, created = Ingredient.objects.get_or_create(name=name, category=category)
        temp.save()


    def handle(self, *args, **options):
        self._create_food_database()

    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    from django.db.models import Q

    managers, created = Group.objects.get_or_create(name='managers')
    
    #permissions_qs = Permission.objects.filter(codename__contains='user')
    permissions_qs = Permission.objects.filter(Q(codename__contains='user') | Q(codename__contains='event')
        | Q(codename__contains='employee') | Q(codename__contains='role') | Q(codename__contains='category') 
        | Q(codename__contains='ingredient') | Q(codename__contains='Ingredient Quantity') | Q(codename__contains='menu')
        | Q(codename__contains='menu item') | Q(codename__contains='recipe') | Q(codename__contains='user profile') 
        | Q(codename__contains='notify') | Q(codename__contains='schedule manager') | Q(codename__contains='session'))

    managers.permissions = permissions_qs
    managers.save() 

    employees, created = Group.objects.get_or_create(name='employees')


    from django.contrib.auth.models import User
    from register.models import UserProfile
    manager = User.objects.create_user(username='manager',
                                 email='manager@catz.com',
                                 password='manager123', first_name='First', last_name='Last')
    manager_profile = UserProfile.objects.get(id=manager.id)
    manager_profile.phone = '+999999999'
    manager_profile.address = 'Managers Address'
    manager_profile.save()
    g = Group.objects.get(name='managers')
    g.user_set.add(manager)

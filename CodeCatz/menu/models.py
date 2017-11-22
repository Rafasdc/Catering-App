from django.db import models
from django.utils.timezone import now
import uuid
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

class Category(TitleSlugDescriptionModel):

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

class Ingredient(TimeStampedModel):
    name=models.CharField(_('Name'), max_length=100)
    description=models.TextField(_('Description'), blank=True, null=True)
    category=models.ForeignKey(Category)

    def __str__(self):
        return self.name

class IngredientQuantity(TimeStampedModel):
    UNIT_CHOICES = (('oz', 'ounce'), ('c', 'cup'), ('lb', 'pound'), ('ts', 'teaspoon'), ('T', 'tablespoon'))
    recipe = models.ForeignKey('Recipe')
    ingredient=models.ForeignKey(Ingredient)
    quantity=models.DecimalField(_('Quantity'), max_digits=5, decimal_places=2)
    unit=models.CharField(_('Unit'), choices=UNIT_CHOICES, max_length=3, blank=True, null=True)

    class Meta:
        verbose_name=_('Ingredient Quantity')
        verbose_name_plural=_('Ingredient Quantities')

    def __str__(self):
        if self.unit:
            return ' '.join([self.ingredient.name, str(self.quantity), self.unit])
        else:
            return ' '.join([str(self.quantity), self.ingredient.name])

class Recipe(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Represent a menu item
    """
    APPROVAL_CHOICES = (
    (u'app', u'Appetizer'),
    (u'lunch', u'Lunch'),
    (u'din', u'Dinner'),
    (u'des', u'Desert'),
    (u'side', u'Side'),
    (u'bfast', u'Breakfast'),
    )

    ingredients = models.ManyToManyField(Ingredient, blank=True, through=IngredientQuantity)
    meal_type = models.CharField(_('Type'), max_length=100, choices=APPROVAL_CHOICES, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Select cost for this menu item.", null=True)
    serves = models.IntegerField(_('Serves'), default=1)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

class MenuItem(TimeStampedModel):
    menu_constituents = models.ManyToManyField(Recipe)

    def __str__(self):
        return ', '.join(x.__str__() for x in self.menu_constituents.all())

    @property
    def menu_items(self):
        items ={}
        for x in self.menu_constituents.all():
            items[x.recipe.title] = x.recipe.recipe_quantities
        
        return items


class Menu(TimeStampedModel, models.Model):
    """
    Represents a Menu of MenuItem
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(_('Title'), max_length=100)
    menu_items = models.ManyToManyField(MenuItem, help_text="Add meal to this menu.")

    @property
    def shopping_list(self):
        pass
    
    @property
    def total_cost(self):
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
    	return reverse('menu-details', args=[str(self.id)])
        
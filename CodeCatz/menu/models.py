from django.db import models
from django.utils.timezone import now
import uuid
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from django_extensions.db.fields import AutoSlugField

class Category(TitleSlugDescriptionModel):

    def __unicode__(self):
        return self.title

class Ingredient(TimeStampedModel):
    name=models.CharField(_('Name'), max_length=100)
    description=models.TextField(_('Description'), blank=True, null=True)
    category=models.ForeignKey(Category)

    def __str__(self):
        return self.name

class IngredientQuantity(TimeStampedModel):
    UNIT_CHOICES = (('oz', 'ounce'), ('c', 'cup'), ('lb', 'pound'), ('ts', 'teaspoon'), ('T', 'tablespoon'))
    ingredient=models.ForeignKey(Ingredient)
    quantity=models.DecimalField(_('Quantity'), max_digits=5, decimal_places=2)
    unit=models.CharField(_('Unit'), choices=UNIT_CHOICES, max_length=3, blank=True, null=True)

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
    (u'bfast', u'Breakfast'),
    )
    ingredient_quantities = models.ManyToManyField(IngredientQuantity, blank=True)
    meal_type = models.CharField(_('Type'), max_length=1, choices=APPROVAL_CHOICES, null=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, help_text="Select cost for this menu item.", null=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

class RecipeQuantity(TimeStampedModel):
    recipe = models.ForeignKey(Recipe)
    recipe_quantities = models.IntegerField(_('Quantity'), default=1)

class MenuItem(TimeStampedModel):
    menu_constituents = models.ManyToManyField(RecipeQuantity)

class Menu(TimeStampedModel, models.Model):
    """
    Represents a Menu of MenuItem
    """
    menu_items = models.ManyToManyField(MenuItem, help_text="Add menu item to this menu.")

    @property
    def shopping_list(self):
        pass
    
    @property
    def total_cost(self):
        pass

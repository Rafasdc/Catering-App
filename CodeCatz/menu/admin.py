from django.contrib import admin
from django import forms

from.models import Category, Ingredient, IngredientQuantity, Recipe, MenuItem, Menu
from .forms import IngredientQuantityForm, CreateMenuItemForm
# Register your models here.

admin.site.register(Category)
admin.site.register(Ingredient)

admin.site.register(Menu)

class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    form = IngredientQuantityForm


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientQuantityInline,)

admin.site.register(Recipe, RecipeAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    form = CreateMenuItemForm
    fields = [('dinner_options', 'lunch_options', 'desert_options', 'appetizer_options', 'side_options', 'breakfast_options')]

admin.site.register(MenuItem, MenuItemAdmin)
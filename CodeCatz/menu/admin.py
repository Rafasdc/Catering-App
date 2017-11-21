from django.contrib import admin
from django import forms

from.models import Category, Ingredient, IngredientQuantity, Recipe, MenuItem, Menu
from .forms import IngredientQuantityForm
# Register your models here.

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(Menu)

class IngredientQuantityInline(admin.TabularInline):
    model = IngredientQuantity
    form = IngredientQuantityForm


class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientQuantityInline,)

admin.site.register(Recipe, RecipeAdmin)
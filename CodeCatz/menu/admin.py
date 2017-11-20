from django.contrib import admin
from django import forms

from.models import Category, Ingredient, IngredientQuantity, Recipe, RecipeQuantity, MenuItem, Menu
# Register your models here.

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(IngredientQuantity)
admin.site.register(RecipeQuantity)
admin.site.register(Recipe)
admin.site.register(MenuItem)
admin.site.register(Menu)
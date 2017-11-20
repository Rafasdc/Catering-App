from django import forms
from menu.models import BaseMenuItem, Menu, MenuItem, MenuItemDecorator, Food

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields ='__all__'

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields ='__all__'

class BaseMenuItemForm(forms.ModelForm):
    class Meta:
        model = BaseMenuItem
        fields ='__all__'

class MenuItemDecoratorForm(forms.ModelForm):
    class Meta:
        model = MenuItemDecorator
        fields ='__all__'

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields ='__all__'
from django import forms
from menu.models import IngredientQuantity, Ingredient

from dal import autocomplete

class IngredientQuantityForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ('__all__')
        widgets = {
            'ingredient': autocomplete.ModelSelect2(url='ingredient-autocomplete',)
        }

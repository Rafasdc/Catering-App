from django.shortcuts import render
from django.urls import reverse_lazy
from dal import autocomplete

from .models import Ingredient
# Create your views here.


class IngredientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Ingredient.objects.none()

        qs = Ingredient.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
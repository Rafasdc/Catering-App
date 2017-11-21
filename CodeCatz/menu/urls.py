from django.conf.urls import url
from django.views.generic import TemplateView

from menu.views import IngredientAutocomplete


urlpatterns = [
     url(r'^ingredient-autocomplete/$', IngredientAutocomplete.as_view(),name='ingredient-autocomplete',),
]
from django.conf.urls import url
from django.views.generic import TemplateView

from menu.views import IngredientAutocomplete, DinnerAutocomplete, DesertAutocomplete
from menu.views import  LunchAutocomplete, AppAutocomplete, SideAutocomplete, BfastAutocomplete
from menu.views import ViewMenuItems, ViewCreateMenuItem, ViewCreateMenu, ViewListMenus
from menu.views import ViewDetailMenu


urlpatterns = [
    url(r'^ingredient-autocomplete/$', IngredientAutocomplete.as_view(),name='ingredient-autocomplete',),
    url(r'^dinner-autocomplete/$', DinnerAutocomplete.as_view(),name='dinner-autocomplete',),
    url(r'^lunch-autocomplete/$', LunchAutocomplete.as_view(),name='lunch-autocomplete',),
    url(r'^desert-autocomplete/$', DesertAutocomplete.as_view(),name='desert-autocomplete',),
    url(r'^app-autocomplete/$', AppAutocomplete.as_view(),name='app-autocomplete',),
    url(r'^side-autocomplete/$', SideAutocomplete.as_view(),name='side-autocomplete',),
    url(r'^bfast-autocomplete/$', BfastAutocomplete.as_view(),name='bfast-autocomplete',),
    url(r'^$', ViewMenuItems.as_view(), name='menu-items'),
    url(r'^create_item/$', ViewCreateMenuItem.as_view(), name='menu-item-create'),
    url(r'^create_menu/$', ViewCreateMenu.as_view(), name='menu-create'),
    url(r'^menus/$', ViewListMenus.as_view(), name='menu-options'),
    url(r'^menu/(?P<pk>\d+)$', ViewDetailMenu.as_view(), name='menu-details'),
]
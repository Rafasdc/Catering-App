from django.shortcuts import render
from django.urls import reverse_lazy
from dal import autocomplete

from menu.models import *
from menu.forms import *
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

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

class DinnerAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='din')

        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs

class LunchAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='lun')
        
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs

class DesertAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='des')
        
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs

class AppAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='app')
        
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs

class SideAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='side')
        
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs

class BfastAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recipe.objects.none()

        qs = Recipe.objects.filter(meal_type='bfast')
        
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs


class ViewMenuItems(TemplateView):
    """
    Plain view of all menu items
    """
    template_name = 'menu/menu.html'

    def get_context_data(self, **kwargs):
        context = super(ViewMenuItems, self).get_context_data(**kwargs)
        context['Dinner'] = Recipe.objects.filter(meal_type='din')
        context['Lunch'] = Recipe.objects.filter(meal_type='lunch')
        context['Desert'] = Recipe.objects.filter(meal_type='des')
        context['App'] = Recipe.objects.filter(meal_type='app')
        context['Side'] = Recipe.objects.filter(meal_type='side')
        context['Breakfast'] = Recipe.objects.filter(meal_type='bfast')
        return context

class ViewCreateMenuItem(LoginRequiredMixin, CreateView):
    """
    Recipe to create menu item
    """
    form_class = CreateMenuItemForm
    model = MenuItem
    success_url = reverse_lazy('menu-create')

class ViewCreateMenu(LoginRequiredMixin, CreateView):
    """
    Create a menu
    """
    model = Menu
    fields = '__all__'
    success_url = reverse_lazy('menu-options')

class ViewListMenus(LoginRequiredMixin, generic.ListView):
    """
    View created menus
    """
    model = Menu
    template_name ='menu/predefined_menu_list.html'
    paginate_by = 10

class ViewDetailMenu(LoginRequiredMixin, generic.DetailView):
    model=Menu





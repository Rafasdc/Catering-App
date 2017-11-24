from django import forms
from menu.models import *
from dal import autocomplete

class IngredientQuantityForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantity
        fields = ('__all__')
        widgets = {
            'ingredient': autocomplete.ModelSelect2(url='ingredient-autocomplete',)
        }

class CreateMenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        exclude = ['menu_constituents']
    
    dinner_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='din'), required=False, widget=autocomplete.ModelSelect2Multiple(url='dinner-autocomplete', attrs={'data-placeholder': 'Dinners', 'data-minimum-input-length': 0,}))
    lunch_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='lunch'), required=False, widget=autocomplete.ModelSelect2Multiple(url='lunch-autocomplete', attrs={'data-placeholder': 'Lunches', 'data-minimum-input-length': 0,}))
    desert_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='des'), required=False, widget=autocomplete.ModelSelect2Multiple(url='desert-autocomplete', attrs={'data-placeholder': 'Desert', 'data-minimum-input-length': 0,}))
    appetizer_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='app'), required=False, widget=autocomplete.ModelSelect2Multiple(url='app-autocomplete', attrs={'data-placeholder': 'Appetizers', 'data-minimum-input-length': 0,}))
    side_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='side'), required=False, widget=autocomplete.ModelSelect2Multiple(url='side-autocomplete', attrs={'data-placeholder': 'Sides', 'data-minimum-input-length': 0,}))
    breakfast_options =  forms.ModelMultipleChoiceField(queryset=Recipe.objects.filter(meal_type='bfast'), required=False, widget=autocomplete.ModelSelect2Multiple(url='bfast-autocomplete', attrs={'data-placeholder': 'Breakfasts', 'data-minimum-input-length': 0,}))
   
    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['dinner_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
            initial['side_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
            initial['lunch_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
            initial['desert_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
            initial['appetizer_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
            initial['breakfast_options'] = [t.pk for t in kwargs['instance'].menu_constituents.all()]
        super(CreateMenuItemForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        instance = super(CreateMenuItemForm, self).save(commit=False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.menu_constituents.clear()
            for x in self.cleaned_data['dinner_options']:
                instance.menu_constituents.add(x)
            for x in self.cleaned_data['lunch_options']:
                instance.menu_constituents.add(x)
            for x in self.cleaned_data['desert_options']:
                instance.menu_constituents.add(x)
            for x in self.cleaned_data['appetizer_options']:
                instance.menu_constituents.add(x)
            for x in self.cleaned_data['side_options']:
                instance.menu_constituents.add(x)
            for x in self.cleaned_data['breakfast_options']:
                instance.menu_constituents.add(x)

        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()


        return instance

class CreateMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'menu_items']
    
    def save(self, user=None):
        menu = super(CreateMenuForm, self).save(commit=False)
        if user:
            menu.user = user
        menu.save()
        self.save_m2m()
        return menu
        

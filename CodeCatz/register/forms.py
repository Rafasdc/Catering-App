from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Use a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1',]:
            self.fields[fieldname].help_text = "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information."

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'password1', 'password2', )
        help_texts = {
            'password1': "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information.",
}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        #required = {'email':True,}
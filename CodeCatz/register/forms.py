from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    bio = forms.CharField(widget=forms.Textarea, required=False, help_text='Talk about yourself.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1',]:
            self.fields[fieldname].help_text = "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information."

    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'birth_date','location', 'bio', 'password1', 'password2', )
        help_texts = {
            'password1': "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information.",
        }
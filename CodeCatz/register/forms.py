from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Use a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in [ 'password1',]:
            self.fields[fieldname].help_text = "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information."

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
        help_texts = {
            'password1': "Your password must be at least 8 characters, not entirely alphanumeric, commonly used, or similar to personal information.",
        }
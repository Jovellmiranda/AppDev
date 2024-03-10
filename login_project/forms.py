from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=6, required=False, help_text='Optional')
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    age = forms.IntegerField(min_value=1, max_value=100, help_text='Enter a valid age')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age', 'password1', 'password2']

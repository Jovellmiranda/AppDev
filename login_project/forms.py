from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

class SignUpForm(UserCreationForm):
    Full_Name = forms.CharField(min_length=6, required=True, help_text='Required')
    Phone_Number = forms.CharField(max_length=30, required=False, help_text='Optional')
    Email_Address = forms.EmailField(max_length=254, required=False, help_text='Optional')
    Date_of_Birth = forms.IntegerField(help_text='Enter your date of birth as a number (DD/MM/YYYY)',
                                       widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}))

    Password = forms.CharField(min_length=8, widget=forms.PasswordInput, help_text='Enter a valid password')

    class Meta:
        model = User
        fields = ['Full_Name', 'Phone_Number', 'Email_Address', 'Date_of_Birth', 'password1', 'password2']

    def clean_Date_of_Birth(self):
        dob_number = self.cleaned_data.get('Date_of_Birth')
        if dob_number:
            try:
                dob_str = str(dob_number)
                dob_combined = datetime.strptime(dob_str, '%d%m%Y').date()
                return dob_combined
            except ValueError:
                raise forms.ValidationError("Invalid date format. Please enter DD/MM/YYYY.")
        return dob_number

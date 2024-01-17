from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Lead

User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age'
        }

        error_messages = {
            'first_name': {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name!"
            },
            'last_name': {
                "required": "Your name must not be empty",
                "max_length": "Please enter a shorter name!"
            }
        }


class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


# creating a custom form to solve the AttributeError at /signup error


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

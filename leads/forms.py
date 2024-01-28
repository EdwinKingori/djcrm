from collections.abc import Mapping
from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms.utils import ErrorList
from .models import Lead, Agent

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


class AssignAgentForm(forms.Form):
    # setting the queryset for the field to an empty queryset (no options are available for selection)
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        # retrieving agents whose organization is associated with the user making the request.
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents

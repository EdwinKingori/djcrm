from django import forms
from .models import Lead


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

from django import forms
from .models import SaltCodeModel
from crispy_forms.helper import FormHelper


class SaltCodeForm(forms.ModelForm):
    class Meta:
        model  = SaltCodeModel
        widgets = {
            'salt_code': forms.Textarea(
                attrs={
                    'cols': 100,
                    'rows': 10,
                    'placeholder': 'Please enter your SALT Plant UML  script here and press `Convert`.'
                }
            ),
        }
        labels = {
            'salt_code': '',
        }
        exclude = ['response', 'display']

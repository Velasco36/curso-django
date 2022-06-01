from dataclasses import field
from tkinter import Widget
from tkinter.tix import Form
from django import forms
from .models import Test

class TestForm(forms.ModelForm):

    class Meta:
        model =Test
        fields = (
            'title',
            'caption',
            'amount',
        )
        widgets = {
            'title' : forms.TextInput(
                attrs= {
                    'placeholder': 'enter text here',                    
                }
            )
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']    
        if amount < 10:
            raise forms.ValidationError('enter a number greater than 10 ')

        return amount

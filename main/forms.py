from django.forms import ModelForm
from django import forms
from main.models import Product

class NotesEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "subject", "description", "price"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'p-2 border border-gray-300 rounded-md w-full'}),
            'subject': forms.TextInput(attrs={'class': 'p-2 border border-gray-300 rounded-md w-full'}),
            'description': forms.Textarea(attrs={'class': 'p-2 border border-gray-300 rounded-md w-full'}),
            'price': forms.NumberInput(attrs={'class': 'p-2 border border-gray-300 rounded-md w-full'}),
        }
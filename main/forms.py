from django.forms import ModelForm
from django import forms
from main.models import Product
from django.utils.html import strip_tags

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
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        return strip_tags(name)
    
    def clean_subject(self):
        subject = self.cleaned_data.get("subject")
        return strip_tags(subject)
    
    def clean_price(self):
        price = self.cleaned_data("price")
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data("description")
        return strip_tags(description)
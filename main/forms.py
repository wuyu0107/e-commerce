from django.forms import ModelForm
from main.models import Product

class NotesEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "subject", "description", "price"]

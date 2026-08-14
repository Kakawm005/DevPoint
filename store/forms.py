from django import forms
from store.models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category' , 'price', 'photo', 'bio', 'stock']
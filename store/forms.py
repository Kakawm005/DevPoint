from django import forms
from store.models import Product, Category

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category' , 'price', 'photo', 'bio', 'stock']

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
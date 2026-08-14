from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from store.models import Product
from store.forms import NewProductForm

class HomeView(TemplateView):
    template_name = 'home.html'


class StoreView(ListView):
    template_name = 'store.html'
    model = Product
    context_object_name = 'product'


class NewProductView(CreateView):
    template_name = 'sell.html'
    model = Product
    form_class = NewProductForm
    success_url = 'home/'
    


class Contact(TemplateView):
    pass

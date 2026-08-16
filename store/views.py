from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from store.models import Product, Category
from store.forms import NewProductForm, NewCategoryForm
from django.urls import reverse_lazy
from django.db.models import Q

class HomeView(TemplateView):
    template_name = 'home.html'


class StoreView(ListView):
    template_name = 'store.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get("search")
        
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query))

        return queryset


class NewProductView(CreateView):
    template_name = 'new_product.html'
    model = Product
    form_class = NewProductForm
    success_url = reverse_lazy('store')
    

class NewCategoryView(CreateView):
    template_name = 'newcategory.html'
    model = Category
    form_class = NewCategoryForm
    success_url = reverse_lazy('store')


class Contact(TemplateView):
    pass

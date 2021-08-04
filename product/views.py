from django.shortcuts import render
from django.views.generic import DetailView, ListView
from product.models import Product


class ProductView(ListView):
    model = Product
    template_name = "product.html"

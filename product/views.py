from django.shortcuts import render
from django.views.generic import DetailView
from product.models import Product


class ProductView(DetailView):
    model = Product
    template_name = "product.html"

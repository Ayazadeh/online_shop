from django.views.generic import ListView
from product.models import Product


class LandingPage(ListView):
    model = Product
    template_name = 'index.html'
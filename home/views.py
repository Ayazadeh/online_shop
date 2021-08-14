from django.views.generic import ListView
from product.models import Product


class LandingPage(ListView):
    template_name = 'index.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.all()[:8]
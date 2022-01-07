from django.urls import path
from django.views.generic import ListView
from . import views
from product.models import Product

app_name = 'home'
urlpatterns = [
    path('', ListView.as_view(template_name='index.html', queryset=Product.objects.all()[:8]),
         name='landing_page'),
    path('about_us/', views.about_us, name='about_us'),
]

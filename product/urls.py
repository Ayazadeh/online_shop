from django.urls import path
from product.views import *

app_name = 'product'
urlpatterns = [
    path('', ProductView.as_view(), name='product')
]

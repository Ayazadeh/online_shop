from django.urls import path
from order.views import add_to_cart, remove_from_cart

app_name = 'order'

urlpatterns = [
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart, name='remove-from-cart'),
]

from django.urls import path
from product.views import *

app_name = 'product'
urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('api/', ProductListApiView.as_view(), name='api'),
    path('api/<str:pk>', ProductDetailApi.as_view(), name='api_detail'),
]

from django.urls import path
from product.views import *

app_name = 'product'
urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('all/api/', ProductListApiView.as_view(), name='api'),
    path('api/<str:pk>', ProductDetailApi.as_view(), name='api_detail'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>', CategoryDetailView.as_view(), name='category_detail')
]

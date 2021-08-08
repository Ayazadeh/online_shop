from django.urls import path
from customer.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='my_login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('user_api/', UserListApi.as_view(), name='users'),
    path('user_api/<int:pk>', UserDetailApi.as_view(), name='user_detail'),
    path('address_api/', AddressListApi.as_view(), name='address'),
    path('address_api/<int:pk>', AddressDetailApi.as_view(), name='address_detail')
]

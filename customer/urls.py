from django.urls import path
from customer.views import *
from django.contrib.auth import views as auth_views

app_name = 'customer'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='my_login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    path('user_api/', UserListApi.as_view(), name='users'),
    path('user_api/<int:pk>', UserDetailApi.as_view(), name='user_detail'),
    path('address_api/', AddressListApi.as_view(), name='address'),
    path('address_api/<int:pk>', AddressDetailApi.as_view(), name='address_detail')
]

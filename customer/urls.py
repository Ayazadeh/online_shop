from django.urls import path
from customer.views import *

urlpatterns = [
    path('login/', Login.as_view(), name='my_login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout')
]

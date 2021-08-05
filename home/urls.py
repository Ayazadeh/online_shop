from django.urls import path
from home.views import *

app_name = 'home'
urlpatterns = [
    path('', LandingPage.as_view(), name='landing_page')
]

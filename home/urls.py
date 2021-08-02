from django.urls import path
from home.views import *

urlpatterns = [
    path('', LandingPage.as_view())
]

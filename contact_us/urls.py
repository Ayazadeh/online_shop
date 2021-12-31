from django.urls import path
from contact_us.views import ContactUsView

app_name = 'contact_us'
urlpatterns = [
    path('', ContactUsView.as_view(), name="contact_us")
]
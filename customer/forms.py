from django.contrib.auth.forms import UserCreationForm
from django import forms
from customer.models import *


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,
                                 required=True)

    last_name = forms.CharField(max_length=50,
                                required=True)

    class Meta:
        model = Customer
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'customer_image']

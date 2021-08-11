from django.contrib.auth.forms import UserCreationForm
from django import forms
from customer.models import *


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = Customer
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  'customer_image']

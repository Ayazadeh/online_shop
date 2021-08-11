from django.contrib import admin
from customer.models import *


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_ptr_id', 'username', 'email', 'is_superuser', 'phone']
    search_fields = ['username', 'phone', 'first_name', 'last_name']
    exclude = ['last_login',
               'is_superuser',
               'groups',
               'user_permissions',
               'is_staff',
               'is_active',
               'date_joined',
               '']


admin.site.register(Customer, CustomerAdmin)

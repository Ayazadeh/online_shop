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


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner_address', 'state', 'city', 'zip_code', 'plaque', 'lat', 'lng']
    search_fields = ['owner_address', 'state', 'city', 'plaque']

    @staticmethod
    def owner_address(obj):
        return obj.owner.username


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)

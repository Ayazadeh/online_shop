from django.contrib import admin
from customer.models import *


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'super_user']
    search_fields = ['user__username']

    def email(self, obj):
        return obj.user.email

    def super_user(self, obj):
        return obj.user.is_superuser


admin.site.register(Customer, CustomerAdmin)

from django.contrib import admin
from customer.models import *


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']


admin.site.register(Customer, CustomerAdmin)

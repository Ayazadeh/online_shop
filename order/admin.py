from django.contrib import admin
from order.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_ordered', 'product', 'quantity']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

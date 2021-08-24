from django.contrib import admin
from order.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner']
    exclude = ['is_deleted', 'delete_timestamp']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'is_ordered', 'product', 'quantity']
    exclude = ['is_deleted', 'delete_timestamp']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

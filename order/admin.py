from django.contrib import admin
from order.models import *


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordered', 'product', 'quantity']


admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
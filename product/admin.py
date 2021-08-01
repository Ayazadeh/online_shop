from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'inventory', 'discount', 'brand', 'category']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'price']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'discount_name', 'amount', 'unit', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'parent']


admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)

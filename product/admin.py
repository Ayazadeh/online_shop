from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'price', 'inventory', 'discount', 'brand', 'category']
    search_fields = ['product_name', 'brand']


class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'price']


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'discount_name', 'amount', 'unit', 'description']
    search_fields = ['discount_name', 'unit']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'parent']
    search_fields = ['category_name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand_name']
    search_fields = ['brand_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)

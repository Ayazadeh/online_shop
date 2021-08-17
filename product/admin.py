from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product_name',
        'price',
        'inventory',
        'discount',
        'brand',
        'category'
    ]

    search_fields = [
        'product_name',
        'price',
        'brand',
        'inventory'
    ]

    fields = [
        'product_name',
        'price',
        'discount',
        'category',
        'inventory',
        'brand',
        'product_image'
    ]


class DiscountAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'discount_name',
        'amount',
        'unit',
        'description'
    ]

    search_fields = ['discount_name', 'unit']

    fields = [
        'discount_name',
        'amount',
        'unit',
        'description',
    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name', 'parent']
    search_fields = ['category_name']
    fields = ['category_name', 'parent']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand_name']
    search_fields = ['brand_name']
    fields = ['brand_name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)

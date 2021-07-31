from django.contrib import admin
from product.models import *

admin.site.register(Product)
admin.site.register(Price)
admin.site.register(Discount)
admin.site.register(Category)
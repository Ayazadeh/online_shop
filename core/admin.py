from django.contrib import admin
from core.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_superuser', 'is_staff']
    search_fields = ['id', 'username']


admin.site.register(User, UserAdmin)

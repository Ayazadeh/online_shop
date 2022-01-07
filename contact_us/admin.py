from django.contrib import admin
from contact_us.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone_number',
        'email',
        'message'
    ]


admin.site.register(ContactUs, ContactUsAdmin)

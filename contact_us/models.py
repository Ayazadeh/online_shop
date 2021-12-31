from core.models import *
from django.utils.translation import gettext_lazy as _


class ContactUs(TimestampMixin):
    class Meta:
        verbose_name = _("Contact Us:")

    name = models.CharField(max_length=50,
                            verbose_name=_('Name:'),
                            null=False,
                            blank=False)

    phone_number = models.CharField(max_length=11,
                                    verbose_name=_("Phone Number:"),
                                    null=False,
                                    blank=False, )

    email = models.EmailField(max_length=250,
                              verbose_name=_("Email:"),
                              null=False,
                              blank=False)

    message = models.TextField(max_length=1000,
                               verbose_name=_("Message:"),
                               null=False,
                               blank=False)

    def __str__(self):
        return f"{self.name} : {self.message}"
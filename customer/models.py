from core.models import *
from customer.validators import *
from django.utils.translation import gettext_lazy as _


class Customer(User, TimestampMixin):
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f'{self.id}# {self.username}'


class Address(TimestampMixin):
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    owner = models.ForeignKey(Customer,
                              on_delete=models.CASCADE,
                              verbose_name=_("Owner:"),
                              help_text=_("choose owner of address!"),
                              null=False,
                              blank=False)

    state = models.CharField(max_length=30,
                             verbose_name=_("State:"),
                             help_text=_("Enter name of state!"),
                             null=False,
                             blank=False)

    city = models.CharField(max_length=30,
                            verbose_name=_("City:"),
                            help_text=_("Enter name of city!"),
                            null=False,
                            blank=False)

    lat = models.FloatField(null=True,
                            verbose_name=_("Latitude"),
                            help_text=_("Enter latitude for address"),
                            blank=True)

    lng = models.FloatField(null=True,
                            verbose_name=_("Longitude"),
                            help_text=_("Enter Longitude for address"),
                            blank=True)

    detail = models.CharField(max_length=150,
                              verbose_name=_("Detail:"),
                              help_text=_("Enter detail for address"),
                              null=True,
                              blank=True)

    zip_code = models.CharField(max_length=10,
                                verbose_name=_("Zip Code:"),
                                help_text=_("Enter zip code for address"),
                                null=False,
                                blank=False,
                                validators=[zip_code_validation]
                                )

    plaque = models.PositiveIntegerField(verbose_name=_("Plaque:"),
                                         help_text=_("Enter plaque for address"),
                                         null=False,
                                         blank=False)

    def __str__(self):
        return f'{self.id}# {self.state}, {self.city}'

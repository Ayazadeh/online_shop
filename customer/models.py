from core.models import *
from customer.validators import *
from django.utils.translation import gettext_lazy as _


def customer_image_path(instance, filename):
    return f'customer/profile/{User.objects.get(id=instance.user_ptr_id).username}/{filename}'


class Customer(User, TimestampMixin):
    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _("Customers")

    customer_image = models.FileField(upload_to=customer_image_path,
                                      default='customer/profile/default.png',
                                      null=True,
                                      blank=True,
                                      validators=[validate_file_extension]
                                      )
    phone = models.CharField(max_length=11,
                             null=False,
                             blank=False,
                             validators=[phone_validation])

    def __str__(self):
        return f'{self.id}# {self.username}'


class Address(TimestampMixin):
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    owner = models.ForeignKey(Customer,
                              on_delete=models.CASCADE,
                              null=False,
                              blank=False)

    state = models.CharField(max_length=30,
                             null=False,
                             blank=False)

    city = models.CharField(max_length=30,
                            null=False,
                            blank=False)

    lat = models.FloatField(null=True,
                            blank=True)

    lng = models.FloatField(null=True,
                            blank=True)

    detail = models.CharField(max_length=150,
                              null=True,
                              blank=True)

    zip_code = models.CharField(max_length=10,
                                null=False,
                                blank=False,
                                validators=[zip_code_validation]
                                )

    plaque = models.PositiveIntegerField(null=False,
                                         blank=False)

    def __str__(self):
        return f'{self.id}# {self.state}, {self.city}'

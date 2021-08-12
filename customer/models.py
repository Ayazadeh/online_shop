from core.models import *
from customer.validators import *


class Customer(User, TimestampMixin):
    customer_image = models.FileField(upload_to='customer/profile',
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

    zip_code = models.PositiveIntegerField(null=False,
                                           blank=False)

    plaque = models.PositiveIntegerField(null=False,
                                         blank=False)

    def __str__(self):
        return f'{self.id}# {self.state}, {self.city}'

from core.models import *
from customer.validators import *


class Customer(TimestampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
        return f'{self.id}# {self.user.username}'


class Address(TimestampMixin):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    state = models.CharField(max_length=30,
                             null=False,
                             blank=False)

    city = models.CharField(max_length=30,
                            null=False,
                            blank=False)

    lat = models.FloatField()
    lng = models.FloatField()
    detail = models.CharField(max_length=100,
                              null=True,
                              blank=True)
    zip_code = models.PositiveIntegerField()
    plaque = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id}# {self.state}, {self.city}'

from core.models import *


class Customer(TimestampMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


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

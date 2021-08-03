from core.models import *


class Customer(User, TimestampMixin):
    pass


class Address(TimestampMixin):
    state = models.CharField(max_length=30,
                             null=False,
                             blank=False)
    city = models.CharField(max_length=30,
                            null=False,
                            blank=False)


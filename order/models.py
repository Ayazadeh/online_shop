from django.core.exceptions import ValidationError
from django.db import models
from core.models import TimestampMixin
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from product.models import Product


class OrderStatus(models.Model):
    status = models.CharField(max_length=30,
                              verbose_name=_("status:"),
                              help_text=_("add status for order's"))

    def __str__(self):
        return f"{self.status}"


def number_item_validator(value):
    if not value > product_item.inverntory:
        raise ValidationError('inventory is not enough !!!')


class Order(TimestampMixin):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("customer:"),
                                 help_text=_("choice customer"))

    product_item = models.ForeignKey(Product,
                                     on_delete=models.CASCADE,
                                     verbose_name=_("item:"),
                                     help_text=_("choice item you want"))

    number = models.PositiveIntegerField(default=1,
                                         verbose_name=_("number:"),
                                         help_text=_("add number of item's"),
                                         validators=[number_item_validator])

    status = models.ForeignKey(OrderStatus,
                               on_delete=models.CASCADE,
                               verbose_name=_("status:"),
                               help_text=_("choose status of order"))

    @classmethod
    def order_by_product_item(cls, id):
        return cls.objects.filter(product_item=id)

    def __str__(self):
        return f'- number:{self.number} - status:{self.status}'

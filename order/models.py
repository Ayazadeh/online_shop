from django.core.exceptions import ValidationError
from django.db import models
from core.models import TimestampMixin
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from product.models import Product


class OrderStatus(models.Model):
    status = models.CharField(max_length=30,
                              verbose_name=_("status:"),
                              help_text=_("add status for order's"),
                              null=False,
                              blank=False)

    def __str__(self):
        return f"{self.status}"


class Order(TimestampMixin):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("customer:"),
                                 help_text=_("choice customer"))
    status = models.ForeignKey(OrderStatus,
                               on_delete=models.CASCADE,
                               verbose_name=_("status:"),
                               help_text=_("choose status of order"))

    items = models.ManyToManyField('OrderItem')
    ordered = models.BooleanField(default=False)

    ordered_date = models.DateTimeField()

    @classmethod
    def order_by_product_item(cls, id):
        return cls.objects.filter(product_item=id)

    def __str__(self):
        return self.status.status


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)

    def number_product_exist(self):
        if self.quantity > self.product.inventory:
            raise ValidationError('inventory is not enough !!!')

    quantity = models.PositiveIntegerField(default=1,
                                           validators=[number_product_exist])

    def __str__(self):
        return f'{self.quantity} of {self.product.product_name}'

from django.core.exceptions import ValidationError
from django.db import models
from core.models import TimestampMixin
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from product.models import Product


class Order(TimestampMixin):
    ref_code = models.CharField(max_length=15,
                                verbose_name=_("reference code:"),
                                help_text=_("add reference code for order"))
    owner = models.ForeignKey(Customer,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name=_("owner:"),
                              help_text=_("choice owner of order"))

    status = models.CharField(max_length=150,
                              verbose_name=_("status:"),
                              help_text=_("add status for order"))

    items = models.ManyToManyField('OrderItem')
    is_ordered = models.BooleanField(default=False)

    ordered_date = models.DateTimeField(auto_now=True)

    # payment_details = models.ForeignKey(Payment, null=True)
    @classmethod
    def order_by_product_item(cls, id):
        return cls.objects.filter(product_item=id)

    @staticmethod
    def total_price(product_id, count):
        price = Product.objects.get(id=product_id).final_price()
        return price * count

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.status


class OrderItem(models.Model):
    is_ordered = models.BooleanField(default=False)

    product = models.OneToOneField(Product,
                                   on_delete=models.SET_NULL,
                                   null=True, )
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def number_product_exist(self):
        if self.quantity > self.product.inventory:
            raise ValidationError('inventory is not enough !!!')

    quantity = models.PositiveIntegerField(default=0,
                                           validators=[number_product_exist])

    def __str__(self):
        return f'{self.quantity} of {self.product.product_name}'

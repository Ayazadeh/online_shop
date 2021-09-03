from django.db import models
from core.models import TimestampMixin
from django.utils.translation import gettext_lazy as _
from customer.models import Customer
from product.models import Product


class Order(TimestampMixin):
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    owner = models.ForeignKey(Customer,
                              on_delete=models.SET_NULL,
                              null=True,
                              verbose_name=_("owner:"),
                              help_text=_("choice owner of order"))

    status = models.CharField(max_length=150,
                              verbose_name=_("status:"),
                              help_text=_("add status for order"))

    items = models.ManyToManyField('OrderItem',
                                   verbose_name=_("item's"),
                                   help_text=_("choose item's you want"))

    is_ordered = models.BooleanField(default=False,
                                     verbose_name=_("ordered:"),
                                     help_text=_("choose True if the order is complete!"))

    ordered_date = models.DateTimeField(auto_now=True,
                                        verbose_name=_("order date:"),
                                        help_text=_("date of order!"))

    # payment_details = models.ForeignKey(Payment, null=True)
    @classmethod
    def order_by_product_item(cls, id):
        return cls.objects.filter(product_item=id)

    def get_cart_items(self):
        return self.items.all()

    def total_price(self):
        return sum([item.final_price() for item in self.items.filter(is_deleted=False)])

    def __str__(self):
        return self.status


class OrderItem(TimestampMixin):
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Item's")

    is_ordered = models.BooleanField(default=False,
                                     verbose_name=_("ordered:"),
                                     help_text=_("choose True if the product is ordered!"))

    product = models.OneToOneField(Product,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   verbose_name=_("Product:"),
                                   help_text=_("choose product you want"))

    date_added = models.DateTimeField(auto_now=True,
                                      verbose_name=_("date added:"),
                                      help_text=_("date added to the order item"))

    date_ordered = models.DateTimeField(null=True,
                                        verbose_name=_("date ordered:"),
                                        help_text=_("Order date"))

    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name=_("quantity:"),
                                           help_text=_("add count of item's you want!"),
                                           null=False,
                                           blank=False
                                           )

    def final_price(self):
        return self.product.final_price() * self.quantity

    def __str__(self):
        return f'{self.quantity} of {self.product.product_name}'

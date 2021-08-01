from core.models import *
from django.utils.translation import gettext_lazy as _
from product.validators import *


class Price(TimestampMixin):
    class Meta:
        verbose_name = _("price")

    amount = models.PositiveIntegerField(verbose_name=_("amount:"),
                                         help_text=_("The number you want to price"),
                                         null=True,
                                         blank=True)

    price = models.PositiveIntegerField(verbose_name=_("price:"),
                                        help_text=_("price of product"),
                                        null=False,
                                        blank=False)

    def __str__(self):
        return f'{self.price}'


class Discount(TimestampMixin):
    class Meta:
        verbose_name = _("discount")

    discount_name = models.CharField(max_length=100,
                                     verbose_name=_("name:"),
                                     help_text=_("name of discount"),
                                     null=True,
                                     blank=True)

    amount = models.PositiveIntegerField(verbose_name=_("amount:"),
                                         help_text=_("amount of discount"),
                                         null=False,
                                         blank=False,
                                         )
    description = models.CharField(max_length=300,
                                   verbose_name=_("description"),
                                   help_text=_("description for discount"),
                                   null=True,
                                   blank=True)

    unit_choices = [
        ('rial', 'rial'),
        ('percent', 'percent')
    ]
    unit = models.CharField(max_length=7,
                            verbose_name=_("unit:"),
                            help_text=_("choice unit of discount"),
                            choices=unit_choices,
                            null=False,
                            blank=False)

    def __str__(self):
        return f"{self.amount} {self.unit}"


class Category(TimestampMixin):
    class Meta:
        verbose_name = _("category")

    category_name = models.CharField(max_length=50,
                                     verbose_name=_("name:"),
                                     help_text=_("name of category"),
                                     )

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name=_("parent:"),
                               help_text=_("choose parent for category"),
                               null=True,
                               blank=True,
                               )

    def __str__(self):
        return f'{self.category_name}'


class Product(TimestampMixin):
    class Meta:
        verbose_name = _("product")

    product_name = models.CharField(max_length=100,
                                    verbose_name=_("name:"),
                                    help_text=_("Enter name of product"))

    brand = models.CharField(max_length=100,
                             verbose_name=_("Brand:"),
                             help_text=_("Enter name of manufacturer"))

    price = models.ForeignKey(Price,
                              on_delete=models.CASCADE,
                              verbose_name=_("price:"),
                              help_text=_("choose price"))

    discount = models.ForeignKey(Discount,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("discount:"),
                                 help_text=_("choose discount"),
                                 )

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("category:"),
                                 help_text=_("choose category"))

    inventory = models.IntegerField(verbose_name=_("Inventory:"),
                                    help_text=_("Inventory of product"))

    product_image = models.FileField(upload_to=f'product_image/',
                                     null=False,
                                     blank=False,
                                     validators=[validate_file_extension])

    def final_and_total_price(self, count):
        total_price = self.price.price * count
        final_price = 0
        if self.discount.unit == 'rial':
            final_price = total_price - self.discount.amount
        elif self.discount.unit == 'percent':
            final_price = total_price - (total_price * self.discount.amount)
        return total_price, final_price

    @classmethod
    def order_by_category(cls, id):
        return cls.objects.filter(category_id=id)

    def __str__(self):
        return f'{self.id}# {self.product_name}'

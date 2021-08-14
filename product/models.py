from django.urls import reverse
from core.models import *
from django.utils.translation import gettext_lazy as _
from product.validators import *
from django.core.exceptions import ValidationError


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
                                         blank=False)

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
        verbose_name_plural = _("categories")

    category_name = models.CharField(max_length=50,
                                     verbose_name=_("name:"),
                                     help_text=_("name of category"),
                                     unique=True,
                                     null=False,
                                     blank=False)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               verbose_name=_("parent:"),
                               help_text=_("choose parent for category"),
                               null=True,
                               blank=True,
                               )

    def get_absolute_url(self):
        return reverse("product:category_detail", args=(self.pk,))

    def __str__(self):
        return f'{self.category_name}'


class Brand(TimestampMixin):
    class Meta:
        verbose_name = _("Brand")

    brand_name = models.CharField(max_length=30,
                                  verbose_name=_("brand:"),
                                  help_text=_("add company"),
                                  null=False,
                                  blank=False
                                  )

    def __str__(self):
        return self.brand_name


def product_image_path(instance, filename):
    return f'product/{instance.category.category_name}/{filename}'


class Product(TimestampMixin):
    class Meta:
        verbose_name = _("product")

    product_name = models.CharField(max_length=100,
                                    verbose_name=_("name:"),
                                    help_text=_("Enter name of product"))

    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              verbose_name=_("Brand:"),
                              help_text=_("choose company"),
                              null=False,
                              blank=False
                              )

    price = models.PositiveIntegerField(verbose_name=_('price:'),
                                        help_text=_("Enter price for product")
                                        )

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
                                    help_text=_("Inventory of product"),
                                    null=False,
                                    blank=False)

    product_image = models.FileField(upload_to=product_image_path,
                                     null=False,
                                     blank=False,
                                     validators=[validate_file_extension])

    def final_price(self):
        price = self.price
        final_price = 0
        if self.discount.unit == 'rial':
            final_price = price - self.discount.amount
        elif self.discount.unit == 'percent':
            final_price = price - (price * (self.discount.amount / 100))
        return final_price

    @classmethod
    def order_by_category(cls, id):
        return cls.objects.filter(category_id=id)

    def __str__(self):
        return f'{self.id}# {self.product_name}'

    def get_add_to_cart_url(self):
        return reverse("order:add-to-cart", kwargs={'pk': self.pk})

    def get_remove_from_cart_url(self):
        return reverse("order:remove-from-cart", kwargs={'pk': self.pk})

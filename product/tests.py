from django.test import TestCase
from product.models import *


class DiscountTest(TestCase):

    def test1_unit_percent(self):
        self.dis1 = Discount.objects.create(amount=0, unit='percent')
        self.dis2 = Discount.objects.create(amount=20, unit='percent')

    def test2_unit_rial(self):
        self.dis1 = Discount.objects.create(amount=0, unit='rial')
        self.dis2 = Discount.objects.create(amount=20, unit='rial')

    def test3_amount_negative(self):
        # This code should give an error
        self.dis1 = Discount.objects.create(amount=-20, unit='rial')
        self.dis1 = Discount.objects.create(amount=-20, unit='percent')


class CategoryTest(TestCase):

    def test1_make_object(self):
        self.cat1 = Category.objects.create(category_name='laptop')


class BrandTest(TestCase):

    def test1_make_object(self):
        self.brand = Brand.objects.create(brand_name='asus')

# class ProductTest(TestCase):
#
#     def setUp(self) -> None:
#         self.discount_1 = Discount.objects.create(
#             amount=20,
#             unit='percent'
#         )
#         self.category_1 = Category.objects.create(
#             category_name='phone'
#         )
#         self.brand_1 = Brand.objects.create(
#             brand_name='LG'
#         )
#         self.product_1 = Product.objects.create(
#             product_name='k4',
#             price=1000000,
#             brand=self.brand_1,
#             discount=self.discount_1,
#             category=self.category_1,
#             product_image=None,
#             inventory=2
#         )
#
#     def test1_final_price(self):
#         self.assertEqual(self.product_1.final_price(), 7000000)

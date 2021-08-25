from django.test import TestCase
from customer.models import Customer
from order.models import Order, OrderItem
from product.models import *


class Subtotal(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(
            username='mohammad',
            password='12345678',
            email='m@gmail.com',
            phone='09123456789'
        )
        print(self.customer)
        self.discount_1 = Discount.objects.create(
            amount=20,
            unit='percent'
        )

        self.category_1 = Category.objects.create(category_name='phone')

        self.brand_1 = Brand.objects.create(brand_name='LG')

        self.product_1 = Product.objects.create(
            product_name='laptop',
            price=30000000,
            brand=self.brand_1,
            discount=self.discount_1,
            category=self.category_1,
            product_image=None,
            inventory=1
        )
        self.product_2 = Product.objects.create(
            product_name='mobile',
            price=5000000,
            brand=self.brand_1,
            discount=self.discount_1,
            category=self.category_1,
            product_image=None,
            inventory=1
        )
        self.order_item_1 = OrderItem.objects.create(
            product=self.product_1,
            quantity=1
        )
        self.order_item_2 = OrderItem.objects.create(
            product=self.product_2,
            quantity=1
        )
        self.order = Order.objects.create(
            owner=self.customer,
            status='pay',
        )
        self.order.items.add(self.order_item_1, self.order_item_2)

    def test1_total_price(self):
        self.assertEqual(self.order_item_1.final_price(), 24000000)

    def test2_total_price(self):
        self.assertEqual(self.order_item_2.final_price(), 4000000)

    def test2_get_cart_total(self):
        self.assertEqual(self.order.total_price(), 28000000)

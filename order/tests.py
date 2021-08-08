from django.test import TestCase
from order.models import *
from customer.models import *


class OrderStatusTest(TestCase):

    def test1_order_status(self):
        self.status = OrderStatus.objects.create(status='pay')


class OrderTest(TestCase):

    def test1_order_obj(self):
        self.customer = Customer.objects.create()

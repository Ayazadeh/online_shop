from django.test import TestCase
from order.models import *
from customer.models import *


class OrderTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create()

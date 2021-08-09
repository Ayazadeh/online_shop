from django.test import TestCase
from customer.models import *


class CustomerTest(TestCase):

    def setUp(self):
        user = User.objects.create(password='1234', )

    def test1_customer_obj(self):
        Customer.objects.create()

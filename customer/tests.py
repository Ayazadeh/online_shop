from django.test import TestCase
from customer.models import *


class CustomerTest(TestCase):

    def test1_customer_obj(self):
        self.test = Customer.objects.create(
            username='mohammad',
            email='m.ayazadeh@gmail.com',
            password='123456789',
            phone='09038586843'
        )

    def test2_customer_obj(self):
        self.test = Customer.objects.create(
            username='mohammad',
            email='m.ayazadeh@gmail.com',
            password='123456789',
            phone='038586843'
        )


class AddressTest(TestCase):

    def setUp(self):
        self.test = Customer.objects.create(
            username='mohammad',
            email='m.ayazadeh@gmail.com',
            password='123456789',
            phone='09038586843'
        )

    def test1_address_obj(self):
        self.address_test = Address.objects.create(
            owner=self.test,
            state='Tehran',
            city='tehran',
            zip_code=123456,
            plaque=10
        )

from django.test import TestCase
from customer.models import *


class CustomerTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            username='mohammad',
            email='m.ayazadeh@gmail.com',
            password='123456789',
            phone='09038586843'
        )
        self.customer.full_clean()

    def test1_customer_email(self):
        self.customer.email = 'm.gmail.com'
        self.assertRaises(ValidationError, self.customer.full_clean)

    def test2_customer_email(self):
        self.customer.email = 'm.@gmail'
        self.assertRaises(ValidationError, self.customer.full_clean)

    def test3_customer_email(self):
        self.customer.email = '@gmail.com'
        self.assertRaises(ValidationError, self.customer.full_clean)

    def test4_customer_obj(self):
        self.customer.phone = '123'
        self.assertRaises(ValidationError, self.customer.full_clean)

    def test5_customer_obj(self):
        self.customer.phone = '12345678901'
        self.assertRaises(ValidationError, self.customer.full_clean)

    def test6_customer_obj(self):
        self.customer.phone = '91234567890'
        self.assertRaises(ValidationError, self.customer.full_clean)


class AddressTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            username='mohammad',
            email='m.ayazadeh@gmail.com',
            password='123456789',
            phone='09038586843'
        )
        self.address_test = Address.objects.create(
            owner=self.customer,
            state='Tehran',
            city='tehran',
            zip_code=1234567890,
            plaque=10
        )
        self.customer.full_clean()
        self.address_test.full_clean()

    def test1_address_zip_code(self):
        self.address_test.zip_code = '123'
        self.assertRaises(ValidationError, self.address_test.full_clean)

    def test2_address_zip_code(self):
        self.address_test.zip_code = 'zip code'
        self.assertRaises(ValidationError, self.address_test.full_clean)

    def test3_address_zip_code(self):
        self.address_test.zip_code = '12zipcode.'
        self.assertRaises(ValidationError, self.address_test.full_clean)
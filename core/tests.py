from django.test import TestCase
from core.models import TestModel


class BaseModelTest(TestCase):

    def setUp(self) -> None:
        self.m1 = TestModel.objects.create()

    def test1(self):
        self.m1.deleted = True
        self.m1.save()
        self.assertEqual(self.m1.deleted, True)

from django.test import TestCase
from core.models import TestModel


class BaseModelTest(TestCase):

    def setUp(self) -> None:
        self.m1 = TestModel.objects.create()

    def test1_get_deleted(self):
        self.m1.is_deleted = True
        self.m1.save()
        self.assertNotIn(self.m1, TestModel.objects.all())

    def test2_filter_deleted(self):
        self.m1.is_deleted = True
        self.m1.save()
        self.assertNotIn(self.m1, TestModel.objects.filter())

    def test4_archive(self):
        self.m1.is_deleted = True
        self.m1.save()  # Deleted !!!
        self.assertIn(self.m1, TestModel.objects.archive())
        self.assertNotIn(self.m1, TestModel.objects.all())
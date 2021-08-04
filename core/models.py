from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()
    deleted = models.BooleanField(default=False)


class TimestampMixin(BaseModel):
    class Meta:
        abstract = True

    Create_timestamp = models.DateTimeField(auto_now_add=True)
    Modify_timestamp = models.DateTimeField(auto_now=True)
    Delete_timestamp = models.DateTimeField(default=False,
                                            null=True,
                                            blank=True, )

    def logical_delete(self):
        self.Delete_timestamp = timezone.now()
        self.save()


class User(AbstractUser):
    phone = models.CharField(max_length=11,
                             null=True,
                             blank=True)


class TestModel(BaseModel):
    pass

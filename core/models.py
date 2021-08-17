from django.contrib.auth.models import AbstractUser, UserManager
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

    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(default=None,
                                            null=True,
                                            blank=True, )

    def logical_delete(self):
        self.deleted = True
        self.delete_timestamp = timezone.now()
        self.save()


class NewUserManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    objects = NewUserManager()


class TestModel(BaseModel):
    pass

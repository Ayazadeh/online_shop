from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

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

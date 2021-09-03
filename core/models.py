from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils import timezone

from core.validators import *
from django.utils.translation import gettext_lazy as _


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def archive(self):
        return super().get_queryset()


class BaseModel(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(default=False)
    objects = BaseManager()


class TimestampMixin(BaseModel):
    class Meta:
        abstract = True

    create_timestamp = models.DateTimeField(auto_now_add=True,
                                            verbose_name=_("create date:"))

    modify_timestamp = models.DateTimeField(auto_now=True,
                                            verbose_name=_("update date:"))

    delete_timestamp = models.DateTimeField(default=None,
                                            verbose_name=_("delete date:"),
                                            null=True,
                                            blank=True, )

    def logical_delete(self):
        self.is_deleted = True
        self.delete_timestamp = timezone.now()
        self.save()


class NewUserManager(UserManager):

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        return super().create_superuser(username, email, password, **extra_fields)


def customer_image_path(instance, filename):
    return f'customer/profile/{User.objects.get(id=instance.user_ptr_id).username}/{filename}'


class User(AbstractUser):
    objects = NewUserManager()

    image = models.FileField(upload_to=customer_image_path,
                             default='customer/profile/default.png',
                             verbose_name=_("Image:"),
                             help_text=_("choose image for profile"),
                             null=True,
                             blank=True,
                             validators=[validate_file_extension]
                             )
    phone = models.CharField(max_length=11,
                             verbose_name=_("Phone:"),
                             help_text=_("Enter phone number"),
                             null=False,
                             blank=False,
                             validators=[phone_validation])


class TestModel(BaseModel):
    pass

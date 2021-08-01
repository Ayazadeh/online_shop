from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True


class TimestampMixin(BaseModel):
    class Meta:
        abstract = True

    Create_timestamp = models.DateTimeField(auto_now_add=True)
    Modify_timestamp = models.DateTimeField(auto_now=True)
    Delete_timestamp = models.DateTimeField(default=False,
                                            null=True,
                                            blank=True,
                                            )

    def logical_delete(self):
        self.Delete_timestamp = timezone.now()
        self.save()

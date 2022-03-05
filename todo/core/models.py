from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Todo(BaseModel):
    description = models.CharField(max_length=255)
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

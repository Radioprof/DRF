from django.db import models
from uuid import uuid4


class UserModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=64, blank=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256, blank=False, unique=True)

    def __str__(self):
        return self.username

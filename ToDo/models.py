from django.db import models
from users.models import UserModel

class Project(models.Model):
    name = models.CharField(max_length=32)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(blank=False)

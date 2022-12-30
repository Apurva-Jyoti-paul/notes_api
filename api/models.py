from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=80,default='untitled')
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title+': '+self.body[0:30]
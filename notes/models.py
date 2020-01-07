from django.db import models
from uuid import uuid4

from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    # to add a new subtitle after the migration has been created you must add a default value or go blank=true
    subtitle = models.CharField(max_length=200, default="If you don't know what to say")
    content = models.TextField(blank=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

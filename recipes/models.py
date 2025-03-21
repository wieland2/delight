from django.db import models
import uuid



class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    instruction = models.TextField(max_length=1000)
    prep_time = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100)
    serving = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

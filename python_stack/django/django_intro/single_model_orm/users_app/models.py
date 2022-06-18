from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Move(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
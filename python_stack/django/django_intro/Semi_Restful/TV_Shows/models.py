from distutils.text_file import TextFile
from turtle import title
from django.db import models
from django.forms import CharField, DateField

# Create your models here.

class ShowManager(models.Manager):
    def validator(self,postData):
        errors = {}
        if len(postData["title"]) < 1:
            errors["title"] = "Title field is empty"
        if len(postData["network"]) < 1:
            errors["network"] = "Network Field is empty"
        if len(postData["desc"]) < 1:
            errors["desc"] = "Description Field is empty"
        if len(postData["release_date"]) < 1:
            errors["release_date"] = "Release Date field is empty"
        if len(postData["release_date"]) < 1:
            errors["release_date"] = "Release Date field is empty"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=128)
    network = models.CharField(max_length=128)
    release_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    object = ShowManager()

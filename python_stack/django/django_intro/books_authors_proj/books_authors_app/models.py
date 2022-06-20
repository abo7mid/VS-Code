from enum import auto
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)



class Author(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    books = models.ManyToManyField(Book, related_name="authors")

    



































    #     desc = models.TextField()
    # notes = models.CharField(max_length=20,blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)



    #     created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
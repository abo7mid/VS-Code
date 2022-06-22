from enum import auto
from django.db import models

# Create your models here.


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if not postData['title']:
            errors['title'] = "Please enter book title"
        elif len(postData['title']) < 2:
            errors["title"] = "Book Title should be at least 2 characters"
        if not postData['desc']:
            errors['desc'] = "Please enter book Description"
        elif len(postData['desc']) < 2:
            errors["desc"] = "Book description should be at least 2 characters"
        
        try:
            book = Book.objects.get(title=postData['title'])
            errors['title'] = "This title is already exist!"

        except Book.DoesNotExist:
            pass

        return errors



class AuthorManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if not postData['firstname']:
            errors['firstname'] = "Please enter FirstName"
        elif len(postData['firstname']) < 2:
            errors["firstname"] = "First Name should be at least 2 characters"
        if not postData['lastname']:
            errors['lastname'] = "Please enter LastName"
        elif len(postData['lastname']) < 2:
            errors["lastname"] = "Last Name should be at least 2 characters"
        if not postData['notes']:
            errors["notes"] = "Notes should be filled up"
        return errors


class Book(models.Model):
    title = models.CharField(max_length=60)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()    # add this line for validation!


class Author(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    notes = models.CharField(max_length=20)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()    # add this line!

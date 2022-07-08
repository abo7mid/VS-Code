from django.db import models
import re


class UserManager(models.Manager):
    def validate(self, pData):
        errors = {}
        if len(pData['firstname']) < 2:
            errors['firstname'] = "Firstname should be at least 2 characters"

        if len(pData['lastname']) < 2:
            errors['lastname'] = "Lastname should be at least 2 characters"

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(pData["email"]):
            errors["email"] = "Please enter a valid email address"

        if len(pData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"

        if pData['password'] != pData['confirmPassword']:  # ????
            #     print(type(pData['passwrod']),pData['passwrod'])
            errors['confirmPassword'] = "Passwords does not match"
        return errors


class BookManager(models.Manager):
    def validate(self, pData):
        errors = {}
        if len(pData['title']) < 1:
            # pData['title'] = "title is required" This QueryDict instance is immutable
            errors['title'] = "title is required"
        if len(pData['desc']) < 5:
            errors['desc'] = "description must be at lest 5 charachters"
        return errors


# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # books_uploaded = a list of all books uploaded by a given user
    # user: User.objects.first().books_uploaded.all()
    # liked_books    = a list of all books a user likes
    # User.objects.first().liked_books.all()

    
    


class Book(models.Model):
    title = models.CharField(max_length=64)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    # To get the user who uploaded a book: Book.objects.first().uploaded_by
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    # To get the list of users who like a book: Book.objects.first().users_who_like.all()
    objects = BookManager()

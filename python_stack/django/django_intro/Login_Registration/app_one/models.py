import re
from django.db import models


# Create your models here.

class UserManager(models.Manager):
    def validate(self,pData):
        errors = {}
        if len(pData['firstname']) < 2:
            errors['firstname'] = "Firstname should be at least 2 characters"

        if len(pData['lastname']) < 2:
            errors['lastname'] = "Lastname should be at least 2 characters"
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(pData["email"]):
            errors["email"] = "Please enter a valid email address"


        if len(pData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"

        if pData['password'] != pData['confirmPassword']: #????
        #     print(type(pData['passwrod']),pData['passwrod'])
            errors['confirmPassword'] = "Passwords does not match"


        return errors


class User(models.Model):
    username = models.CharField(max_length=8)
    email = models.CharField(max_length=8)
    firstname = models.CharField(max_length=8)
    lastname = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    objects = UserManager()
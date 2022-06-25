import datetime
from distutils.text_file import TextFile
from turtle import title
from django.db import models
from django.forms import CharField, DateField
import time

# Create your models here.

class ShowManager(models.Manager):
    def validator(self,postData):
        errors = {}
        print("Release Date ",postData['release_date'])
        if len(postData["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData["network"]) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if postData["desc"]:    # description is optional 
            if len(postData["desc"]) < 10:  # but if present must be at least 10
                errors["desc"] = "Description should be at least 10 characters"
        if (postData["release_date"]) == "":
            errors["release_date"] = "Release Date field is empty"
        else:
            currDate = str(datetime.date.today())
            print(f"current date {currDate}")
            print(f"selected date {postData['release_date']}")
            currTs = time.mktime(datetime.datetime.strptime(currDate, "%Y-%m-%d").timetuple())
            selectedTs = time.mktime(datetime.datetime.strptime(postData["release_date"], "%Y-%m-%d").timetuple())
            print(f"current Timestamp {currTs}")
            print(f"selected Timestamp {selectedTs}")
            if currTs < selectedTs:
                print("Date should not be in future") 
                errors["release_date"] = "Date should not be in future"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=128)
    network = models.CharField(max_length=128)
    release_date = models.DateField()
    desc = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    object = ShowManager()

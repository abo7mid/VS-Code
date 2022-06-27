from re import T
from django.db import models

# Create your models here



class CourseManager(models.Manager):
    def basic_validator(self,pData):
        errors = {}
        if len(pData['name']) < 5:
            errors['name'] = "course name must be more than 5 characters!"
        if len(pData['desc']) < 15:
            errors['desc'] = "course description must be more than 15 characters!"
        return errors


class Description(models.Model):
    DescText = models.TextField()

class Course(models.Model):
    courseName = models.CharField(max_length=64)
    courseDesc = models.OneToOneField(Description,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()


from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.CharField(max_length=5)
    course = models.CharField(max_length=20)


class Employee(models.Model):
    name = models.CharField(max_length=30)
    eno = models.CharField(max_length=5)
    course = models.CharField(max_length=20)

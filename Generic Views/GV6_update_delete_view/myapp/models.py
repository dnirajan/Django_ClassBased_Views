import email
from tkinter import Widget
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    password=models.CharField(max_length=30)
    
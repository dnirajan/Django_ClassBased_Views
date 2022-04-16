from django.db import models

# Create your models here.
from django.urls import reverse


class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

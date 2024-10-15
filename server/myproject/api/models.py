# server/myproject/api/models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    id_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
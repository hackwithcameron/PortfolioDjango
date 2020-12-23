from django.db import models
from django import forms


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    first_Name = models.CharField(max_length=30, unique=True)
    last_Name = models.CharField(max_length=30, unique=True)
    email_Address = models.EmailField(max_length=50, unique=True)
    message = models.CharField(max_length=250)

    Contact = models.Manager()

    def __str__(self):
        return self.first_Name

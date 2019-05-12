from django.db import models

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Contacts(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.email

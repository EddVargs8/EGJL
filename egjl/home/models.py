from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=16)
    email = models.CharField(max_length=16)
    age = models.IntegerField()
    status = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.email + " " + str(self.age) + " " + str(self.status) + " " + str(self.date)

class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    hour = models.DateTimeField(auto_now_add=True)
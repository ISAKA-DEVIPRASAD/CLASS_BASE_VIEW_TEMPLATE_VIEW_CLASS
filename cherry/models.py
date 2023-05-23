from django.db import models

# Create your models here.

class Student(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    sage=models.IntegerField()
    saddress=models.TextField()
    def __str__(self):
        return self.sname
from django.db import models

# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=55)
    roll = models.IntegerField()
    branch = models.CharField(max_length=55)
    course = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    
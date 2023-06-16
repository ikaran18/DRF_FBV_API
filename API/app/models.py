from django.db import models
# Create your models here.

class EmployeeModel(models.Model):
    username = models.CharField(max_length=55)
    email = models.EmailField()
    password = models.CharField(max_length=55)
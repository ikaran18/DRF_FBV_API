from django.db import models

# Create your models here.


class Company(models.Model):
    
    company_name = models.CharField(max_length=55)
    company_work = models.CharField(max_length=55)
    company_id = models.IntegerField()
    company_location = models.CharField(max_length=55)
    
    def __str__(self):
        return self.company_name
    
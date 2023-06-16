from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=55)
    author_name = models.CharField(max_length=55)
    price = models.IntegerField()
    discount = models.IntegerField()
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
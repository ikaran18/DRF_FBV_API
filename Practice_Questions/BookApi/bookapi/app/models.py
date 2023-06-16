from django.db import models

# Create your models here.

class Book(models.Model):
    
    book_name = models.CharField(max_length=55)
    author_name = models.CharField(max_length=55)
    published_date = models.CharField(max_length=55)
    book_price = models.IntegerField()
    
    def __str__(self):
        return self.book_name
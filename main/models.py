from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    synopsis = models.TextField()
    date_added = models.DateField(auto_now_add=True)


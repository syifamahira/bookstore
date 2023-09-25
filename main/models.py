from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()
    synopsis = models.TextField()
    date_added = models.DateField(auto_now_add=True)


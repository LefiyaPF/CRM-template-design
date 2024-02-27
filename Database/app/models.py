from django.db import models

# Create your models here.

class ProductDetails(models.Model):

    ProductName = models.CharField(max_length= 150)
    Description = models.TextField()
    Quatity = models.IntegerField()
    Price = models.IntegerField()
    
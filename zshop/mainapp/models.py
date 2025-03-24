from django.db import models

# Create your models here.

class Product(models.Model):
    name  = models.CharField(max_length=255)
    price = models.FloatField()
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to='products/')
    stock = models.PositiveIntegerField()
    

    def __str__(self):
        return f"products: {self.name}"
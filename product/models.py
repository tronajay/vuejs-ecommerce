from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=20,blank=True,null=True)
    selling_price = models.CharField(max_length=20,blank=True,null=True)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
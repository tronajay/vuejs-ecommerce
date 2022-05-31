from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,blank=True,null=True)
    price = models.CharField(max_length=20,blank=True,null=True)
    selling_price = models.CharField(max_length=20,blank=True,null=True)
    desc = models.CharField(max_length=500)
    feature_img = models.URLField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name
    
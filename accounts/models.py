from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=13)
    company = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
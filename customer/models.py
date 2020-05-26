from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    userName =models.CharField(max_length=40)
    phno = models.BigIntegerField()
    adl1= models.TextField()
    adl2= models.TextField()
    locality = models.CharField(max_length=30)
    city =models.CharField(max_length=20)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.userName

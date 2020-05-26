from django.db import models
from django.contrib.auth.models import User
from retailer.models import Items

# Create your models here.

# This table stores the items of the user temporarily
class Temporder(models.Model):
    user =models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Items, on_delete= models.DO_NOTHING)
    items_id =models.IntegerField(default=0)
    quantity =models.IntegerField()
    def __str__ (self):
        return self.item.name

#This table contains the final orders from all the users

class Order(models.Model):
    user =models.ForeignKey(User, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Items, on_delete= models.DO_NOTHING)
    items_id =models.IntegerField(default=0)
    username= models.CharField(max_length=50,default=None)
    quantity =models.IntegerField()
    def __str__ (self):
        return self.item.name
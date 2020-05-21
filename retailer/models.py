from django.db import models

# Create your models here.

class Items(models.Model):
    name =models.CharField(max_length=30)
    price = models.IntegerField()
    picture = models.ImageField(upload_to='photos/%y/%m/%d',blank =True)
    def __str__(self):
        return self.name
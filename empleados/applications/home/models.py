from turtle import title
from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=250)
    caption = models.CharField( max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.title
        

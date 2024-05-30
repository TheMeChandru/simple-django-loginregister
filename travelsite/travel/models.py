from django.db import models 

# Create your models here.

class Destination(models.Model) :

    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Bike(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()

class Rent(models.Model):
    uname = models.ForeignKey(User, on_delete=CASCADE)
    location=models.CharField(max_length=100)
    starttime=models.DateTimeField()
    endtime=models.DateTimeField()
    hours=models.IntegerField()
    amount=models.IntegerField()
    bike=models.ForeignKey(Bike, on_delete=CASCADE)

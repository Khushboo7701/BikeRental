from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import pre_save
from BikeRenting.utils import unique_slug_generator

class Bike(models.Model):

    name = models.CharField(null=True, max_length=100)
    img = models.ImageField(null=True, upload_to='pics')
    price = models.IntegerField(null=True)
    slug = models.SlugField(null=True, max_length=250, blank=True)

class Rent(models.Model):
    uname = models.ForeignKey(User,null=True, on_delete=CASCADE)
    location=models.CharField(null=True, max_length=100)
    starttime=models.DateTimeField(null=True)
    endtime=models.DateTimeField(null=True)
    hours=models.FloatField(null=True)
    amount=models.IntegerField(null=True)
    bike=models.ForeignKey(Bike, null=True, on_delete=CASCADE)
    slug = models.SlugField(null=True, max_length=250, blank=True)

def bikes_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.name)

pre_save.connect(bikes_slug_generator, sender=Bike)


def rent_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.bike.name)

pre_save.connect(rent_slug_generator, sender=Rent)
from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length=55, choices = (('Nabeul','Nabeul'),('Sousse','Sousse')), blank=True)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    surface = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    type =models.CharField(max_length=55, choices = (('Louer','Louer'),('Vendre','Vendre')), blank=True)
    biens =models.CharField(max_length=55, choices = (('Appartement','Appartement'),('Etage de Villa','Etage de Villa'),('Villa','Villa'),('Villa Inachevée','Villa Inachevée'),('Immeuble','Immeuble')), blank=True)
    placeparking = models.BooleanField(default = False)
    abri = models.BooleanField(default = False)
    cellier = models.BooleanField(default = False)
    jardin = models.BooleanField(default = False)
    piscine = models.BooleanField(default = False)
    terasse = models.BooleanField(default = False)
    balcon = models.BooleanField(default = False)


    def __str__(self):
        return self.title

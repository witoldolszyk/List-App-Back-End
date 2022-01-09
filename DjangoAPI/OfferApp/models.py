from django.db import models

# Create your models here.

class Categories(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=100)
    Ordering = models.CharField(max_length=100)

class Offers(models.Model):
    OfferId = models.AutoField(primary_key=True)
    OfferTitle = models.CharField(max_length=100)
    OfferDescription = models.CharField(max_length=100)
    OfferPrice = models.CharField(max_length=100)
    OfferCreated = models.CharField(max_length=100)
from rest_framework import serializers
from OfferApp.models import Categories, Offers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('CategoryId',
                  'CategoryName',
                  'Ordering')

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('OfferId',
                  'OfferTitle',
                  'OfferDescription',
                  'OfferPrice',
                  'OfferCreated')
                  
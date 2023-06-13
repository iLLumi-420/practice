from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [ 'title', 'description', 'price', 'slug' ]

class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model =  Category
        fields = '__all__'      
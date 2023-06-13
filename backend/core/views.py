from django.shortcuts import render
from rest_framework import generics

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializers

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
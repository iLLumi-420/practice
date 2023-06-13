from django.contrib import admin
from .models import Category, Product, ProductSpecification, ProductType, ProductSpecificationValue
# Register your models here.

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(ProductSpecification)
admin.site.register(Product)
admin.site.register(ProductSpecificationValue)


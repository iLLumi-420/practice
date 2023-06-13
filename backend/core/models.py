from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ProductType(models.Model):

    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class ProductSpecification(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name
 

    
class Product(models.Model):

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
    

class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value= models.CharField(max_length=255)

    def __str__(self):
        return self.value







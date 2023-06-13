from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductList.as_view() , name="product"),
    path('category', views.CategoryList.as_view(), name='Category')
]
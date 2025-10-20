from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    """получение списка категорий и создания категории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    """получение списка продуктов и создания продукта"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """получение продукта по id, обновление и удаление продукта"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer

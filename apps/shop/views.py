from django.views.generic import TemplateView, DetailView
from rest_framework import generics
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    """Получение списка категорий и создание новой категории"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    """
    Главная страница.
    Возвращает все доступные товары с фильтрацией по категории, бренду и т.п.
    """
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)

        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        brand = self.request.query_params.get('brand')
        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        color = self.request.query_params.get('color')
        if color:
            queryset = queryset.filter(color__icontains=color)

        return queryset


class ProductDetailAPIView(generics.RetrieveAPIView):
    """Детальная страница товара (по id)"""
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    lookup_field = "pk"


class IndexView(TemplateView):
    """Главная страница """
    template_name = "shop/index.html"


class ProductDetailView(DetailView):
    """Детальная страница товара"""
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"

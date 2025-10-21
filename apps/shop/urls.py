from django.urls import path
from .views import (
    CategoryListAPIView, ProductListAPIView, ProductDetailAPIView,
    IndexView, ProductDetailView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),


    path('api/categories/', CategoryListAPIView.as_view(), name='api-categories'),
    path('api/products/', ProductListAPIView.as_view(), name='api-products'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),
]

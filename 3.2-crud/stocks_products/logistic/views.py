from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.pagination import LimitOffsetPagination


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    # при необходимости добавьте параметры фильтрации
    search_fields = ['id', 'title', 'description']
    pagination_class = LimitOffsetPagination

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products']
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации

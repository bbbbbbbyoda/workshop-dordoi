import django_filters
from .models import Product, Category
from django import forms


class ProductListFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = [
            'sex',
            'category',
        ]

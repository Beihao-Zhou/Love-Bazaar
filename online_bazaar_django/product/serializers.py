from re import T
from django.db import models
from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        use_url=True
    )
    class Meta:
        model = Product
        fields = (
            "id", 
            "name", 
            "category",
            "get_absolute_url", 
            "description", 
            "price", 
            "quantity",
            "image",
            "get_image", 
            "get_thumbnail"
        )
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id", 
            "name", 
            "slug", 
            "get_absolute_url",
            "products"
        )
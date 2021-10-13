from rest_framework import serializers
from .models import Category, Products
from .models import Reviews
from .models import ShoppingCart

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price', 'description']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'user', 'product', 'comment', 'rating']

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'user', 'product', 'quantity']
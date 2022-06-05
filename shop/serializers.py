from rest_framework import serializers
from .models import Shop, Product, Category


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['title', 'city', 'address', 'owner_id']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created', 'updated', 'shop_id']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']

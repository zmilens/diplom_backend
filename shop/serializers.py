from rest_framework import serializers
from authorization.models import Account

from authorization.serializers import AccountSerializer
from .models import Shop, Product, Category, Staff


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

class OperatorSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Account
        fields = ['name', 'last_name', 'email', 'is_staff', 'phone']

class StaffSerializer(serializers.ModelSerializer):

    operator = OperatorSerializer()

    class Meta:
        model = Staff
        fields = ['operator']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'image', 'description', 'price', 
        'stock', 'available', 'created', 'updated', 'shop_id']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']

from itertools import product
from rest_framework import serializers

from authorization.serializers import AccountSerializer
from shop.serializers import ProductSerializer
from .models import Cart, CartProduct, Order, ProductsInOrder

class ProductsInOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsInOrder
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    products = ProductsInOrderSerializer()
    customer = AccountSerializer()

    class Meta:
        model = Order
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    
    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'qty', 'final_price']

class CartSerializer(serializers.ModelSerializer):


    products = CartProductSerializer(many=True)
    owner = AccountSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

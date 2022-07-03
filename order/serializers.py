from rest_framework import serializers
from .models import Order, OrderProduct
from shop.serializers import ProductSerializer
from authorization.serializers import AccountSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderProduct
        fields = ['product', 'qty', 'final_price']

class OrderSerializer(serializers.ModelSerializer):

    products = OrderProductSerializer(many=True)
    # products = CartProductSerializer()
    owner = AccountSerializer()

    class Meta:
        model = Order
        fields = ['id', 'products', 'final_price' , 'created', 'status', 'owner']

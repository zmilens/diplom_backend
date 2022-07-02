from rest_framework import serializers
from .models import Order, ProductsInOrder
from authorization.serializers import AccountSerializer


class ProductsInOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductsInOrder
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    products = ProductsInOrderSerializer(many=True)
    # products = CartProductSerializer()
    customer = AccountSerializer()

    class Meta:
        model = Order
        fields = '__all__'
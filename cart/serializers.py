from itertools import product
from rest_framework import serializers

from authorization.serializers import AccountSerializer
from shop.serializers import ProductSerializer
from .models import Cart, CartProduct

class CartProductSerializer(serializers.ModelSerializer):

    product = ProductSerializer()
    
    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'qty', 'final_price', 'cart', 'user']

class CartSerializer(serializers.ModelSerializer):


    products = CartProductSerializer(many=True)
    # owner = AccountSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

    # def save(self):
    #     cart = Cart()
    #     cart.owner=self.validated_data['owner']
    #     print(cart.owner)
    #     cart.save()
    #     return cart

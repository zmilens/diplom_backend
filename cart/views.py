from django.http import JsonResponse
from requests import request
from authorization.models import Account
from cart.models import Cart, CartProduct
from cart.serializers import CartProductSerializer, CartSerializer
from shop import serializers
import decimal
from shop.models import Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from shop.serializers import ProductSerializer
    
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CartApi(request, id=0):
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'Не авторизован'}, status=401)
    acc = Account.objects.get(id=request.user.id)
    #ищу корзину пользователя
    try:
        cart = Cart.objects.get(owner=acc)
    #создаю корзину, если ее нет 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(owner=acc)
        cart.owner=acc
    serializer_cart = CartSerializer(cart)
    if request.method == 'GET':
        serializer_class = CartSerializer(cart)
        return Response( serializer_class.data, status=200)
    elif request.method == 'POST':
        # reqData = { qty: number, productId: number }
        product_data = JSONParser().parse(request)

        try:
            product = Product.objects.get(id=product_data['productId'])
        except:
            return JsonResponse({ 'message': 'Товар не найден'  }, status=400)
        serializer_product = ProductSerializer(product)
        
        try:
            cartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
            serializer_cartProduct = CartProductSerializer(cartProduct)
            CartProduct.objects.filter(product=product_data['productId'], cart=cart).update(qty=serializer_cartProduct.data['qty'] + 
                                                                                product_data['qty'], 
                                                                                final_price=decimal.Decimal(serializer_cartProduct.data['qty']+product_data['qty']) 
                                                                                * decimal.Decimal(serializer_product.data['price']))
        except CartProduct.DoesNotExist:
            cartProduct = CartProduct.objects.create(product=product, cart=cart, qty=product_data['qty'], final_price=product_data['qty']*serializer_product.data['price'], user=acc)
            cart.products.add(cartProduct)

        cart.save()
        return JsonResponse({'message': serializer_cart.data}, status=200)

    elif request.method == 'DELETE':
        # { productId: number }
        product_data = JSONParser().parse(request)
        cart.products.filter(product=product_data['productId']).delete()
        cart.save()
        return JsonResponse({'message': "Товар удален из корзины!"}, safe=False)

    elif request.method == 'PUT':
        # { productId: number, qty: number }
        product_data = JSONParser().parse(request)
        cartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
        product = Product.objects.get(id=product_data['productId'])
        serializer_product = ProductSerializer(product)
        CartProduct.objects.filter(product=product_data['productId'], cart=serializer_cart.data['id']).update(qty=product_data['qty'], final_price=decimal.Decimal(product_data['qty']) * decimal.Decimal(serializer_product.data['price']))
        newCartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
        serializer_cartProduct = CartProductSerializer(newCartProduct)
        cart.save()
        return JsonResponse({'product': serializer_cartProduct.data}, status=200)
        
    return JsonResponse({'message': 'Method not found'}, status=404)

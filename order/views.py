from django.shortcuts import render
from django.http import JsonResponse
from requests import Response
from authorization.models import Account
from cart.models import Cart, CartProduct
from cart.serializers import CartProductSerializer
from shop.models import Product, Staff
from .models import Order, OrderProduct
from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CheckoutApi(request, id=0):
    if request.method == 'POST':
        acc = Account.objects.get(id=request.user.id)
        cart = Cart.objects.get(owner=request.user.id)  
        # serializer_cart = CartSerializer(cart)
        order = Order.objects.create(owner=acc, shop_id=1)
        serializer_order = OrderSerializer(order)
        
        cartProducts = CartProduct.objects.filter(cart=cart)
        serializer_cartProducts = CartProductSerializer(cartProducts, many=True)
        for productData in serializer_cartProducts.data:
            print(1)
            product = Product.objects.get(id=productData['product']['id'])
            orderProduct = OrderProduct.objects.create(order=order, product=product, qty=productData['qty'], final_price=productData['final_price'], user=acc)
            order.products.add(orderProduct)
        order.save()
        cart.delete()
        

        return JsonResponse(serializer_order.data,status=201)

    if request.method == 'GET':
        orders = Order.objects.filter(owner=request.user.id)
        serializer_orders = OrderSerializer(orders, many=True)
        return JsonResponse(serializer_orders.data, safe=False, status=200)
    return JsonResponse({}, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def OrderApi(request, id=0):
    if request.method=='GET':
        acc = Account.objects.get(id=request.user.id)
        staff = Staff.objects.get(operator=acc)
        order = Order.objects.filter(shop=staff.shop)
        # staff = Staff.objects
        order_serializer = OrderSerializer(order, many=True)
        print(staff.shop)
        print(order)
        return JsonResponse(order_serializer.data, safe=False)
from django.shortcuts import render
from django.http import JsonResponse
from pyparsing import Or
from requests import Response
from authorization.models import Account
from cart.models import Cart
from cart.serializers import CartSerializer
from shop.models import Staff
from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CheckoutApi(request, id=0):
    if request.method == 'POST':
        acc = Account.objects.get(id=request.user.id)
        cart = Cart.objects.get(owner=request.user.id)
        serializer_cart = CartSerializer(cart)
        order = Order.objects.create(customer=acc, shop_id=1)
        serializer_order = OrderSerializer(order)
        return JsonResponse(serializer_order.data,status=201)

    if request.method == 'GET':
        orders = Order.objects.filter(customer=request.user.id)
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
        print(staff.shop)
        print(order)
        return JsonResponse('good', safe=False)

# def StaffApi(request, id=0):
#     if request.method=='GET':
#         owner = Account.objects.get(id=request.user.id)
#         shop = Shop.objects.get(owner=owner)
#         print(shop)
#         staff = Staff.objects.filter(shop=shop)
#         # staff = Staff.objects.all()
#         # if staff.shop==shop:
#         serializer = StaffSerializer(staff, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method=='PUT':
#         print(request.data)
#         operator_data = request.data
#         staff = Staff.objects.get(operator=operator_data['operator'])
#         operator = Account.objects.get(email=staff.operator)
#         operator.is_active=operator_data['is_active']
#         print(operator.is_active)
#         return JsonResponse("Доступ изменен", safe=False)
#     return JsonResponse("not ok", safe=False)
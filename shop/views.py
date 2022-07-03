from ast import operator
from unicodedata import category
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from authorization.models import Account
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer, StaffSerializer, OperatorSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Shop, Product, Category, Staff
from django.core.files.storage import default_storage

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def StaffApi(request, id=0):
    if request.method=='GET':
        owner = Account.objects.get(id=request.user.id)
        shop = Shop.objects.get(owner=owner)
        print(shop)
        staff = Staff.objects.filter(shop=shop)
        # staff = Staff.objects.all()
        # if staff.shop==shop:
        serializer = StaffSerializer(staff, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='PUT':
        print(request.data)
        # operator_data =JSONParser().parse(request)
        operator_data = request.data
        staff = Staff.objects.get(operator=operator_data['operator'])
        operator = Account.objects.get(email=staff.operator)
        print(operator.is_active)
        operator.is_active=operator_data['is_active']
        print(operator.is_active)
        operator_serializers = OperatorSerializer(operator, operator_data)
        operator.save()
        # if operator_serializers.is_valid():
        #     operator_serializers.save()
        #     print(operator_serializers.data)
        #     return JsonResponse("Доступ изменен", operator_serializers.data, safe=False)
        return JsonResponse({"Статус изменен на:": operator.is_active}, safe=False)
        # print(operator_serializers.data)
    return JsonResponse("not ok", safe=False)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ShopApi(request, id=0):
    if request.user.is_authenticated:
        if request.method=='GET':
            shops = Shop.objects.all()
            serializer = ShopSerializer(shops, many=True)
            return JsonResponse(serializer.data, safe=False)
        elif request.method=='POST':
            shop_data=JSONParser().parse(request)
            serializer = ShopSerializer(data=shop_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("Магазин добавлен успешно!", safe=False)
            return JsonResponse("Магазин не добавлен.", safe=False)
        elif request.method=='PUT':
            shop_data = JSONParser().parse(request)
            shops = Shop.objects.get(id=shop_data['id'])
            serializer = ShopSerializer(shops, data=shop_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("Информация об магазине обновлена успешно!", safe=False)
            return JsonResponse("Информация об магазине не обновлена.", safe=False)
        elif request.method=='DELETE':
            shops = Shop.objects.get(id=id)
            shops.delete()
            return JsonResponse("Магазин удален из базы данных.", safe=False)


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all().order_by('title')
    serializer_class = ShopSerializer


@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ProductApi(request, id=0):
    if request.method=='GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method=='POST':
        if request.user.is_authenticated:
            product_data=JSONParser().parse(request)
            serializer = ProductSerializer(data=product_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("Товар добавлен успешно!", safe=False)
            return JsonResponse("Товар не добавлен.", safe=False)
        return JsonResponse("Пользователь не авторизован", safe=False)
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        products = Product.objects.get(id=product_data['id'])
        serializer = ProductSerializer(products, data=product_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Информация о товаре обновлена успешно!", safe=False)
        return JsonResponse("Информация о товаре не обновлена.", safe=False)
    elif request.method=='DELETE':
        products = Product.objects.get(id=id)
        products.delete()
        return JsonResponse("Товар удален из базы данных.", safe=False)


@csrf_exempt
@api_view(['GET',])
def CategoryApi(request, id=0):
    if request.method=='GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
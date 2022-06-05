from unicodedata import category
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import ShopSerializer, ProductSerializer, CategorySerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import Shop, Product, Category


@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ShopApi(request, id=0):
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
        product_data=JSONParser().parse(request)
        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Товар добавлен успешно!", safe=False)
        return JsonResponse("Товар не добавлен.", safe=False)
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
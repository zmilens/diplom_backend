from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer, AccountSerializer
from django.contrib.auth.models import Group
from shop.views import ShopApi
from .models import Account
from rest_framework.parsers import JSONParser

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        print(request.data)
        serializer_account = RegistrationSerializer(data=request.data)
        data = {}
        if serializer_account.is_valid():
            account = serializer_account.save()
            data['response'] = "Новый пользователь успешно зарегистрирован"
            data['email'] = account.email
            data['phone'] = account.phone
            data['name'] = account.name
            data['last_name'] = account.last_name
            data['group'] = account.group
        else:
            data.serializer.errors
        return Response(data)

@api_view(['GET'])
def userdata_view(request):
    if request.user.is_authenticated:
        acc = Account.objects.get(id=request.user.id)
        serializer_account = AccountSerializer(acc)
        return JsonResponse(serializer_account.data, status=200)
    return JsonResponse({'message': 'Не авторизован'}, status=401)

# @api_view(['GET'])
# def userdata_view(request):
#     print(request.user.id)
#     if request.user.is_authenticated:
#         account_data = JSONParser().parse(request)
#         account = Account.objects.get(id=account_data['id'])
#         serializer = AccountSerializer(account, data=account_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(account_data, status=200)
#     return JsonResponse({'message': 'Unauthorized'}, status=401) 

# @csrf_exempt
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def account_view(request, *args, **kwards):
#     context = {}
#     user_id = kwards.get("user_id")
#     try: 
#         account = Account.objects.get(pk=user_id)
#     except Account.DoesNotExist:
#         return HttpResponse("пользователя не существует")
#     if account:
#         context
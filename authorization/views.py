from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegistrationSerializer

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Новый пользователь успешно зарегистрирован"
            data['email'] = account.email
            data['phone'] = account.phone
            data['name'] = account.name
            data['last_name'] = account.last_name
        else:
            data.serializer.errors
        return Response(data)

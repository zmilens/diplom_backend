from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from .views import(registration_view,)
from shop.views import ShopApi

app_name = "authorization"

urlpatterns = [
    path('/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/api/token/verify', TokenVerifyView.as_view(), name='token_verify'), 
    path('/register', registration_view, name="register"),
]
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from cart.views import CartApi

app_name = "cart"

urlpatterns = [
    path('', CartApi),
]
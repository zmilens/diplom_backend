from django.urls import path

from cart.views import CartApi

app_name = "cart"

urlpatterns = [
    path('', CartApi),
]
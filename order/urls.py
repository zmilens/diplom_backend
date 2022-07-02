from django.urls import path

from order.views import CheckoutApi, OrderApi

app_name = "order"

urlpatterns = [
    path('/checkout', CheckoutApi),
    path('', OrderApi),
]
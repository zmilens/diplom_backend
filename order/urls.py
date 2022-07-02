from django.urls import path

from .views import OrderApi

app_name = "order"

urlpatterns = [
    path('', OrderApi),
]
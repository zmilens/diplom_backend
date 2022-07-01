from django.urls import include, path
from .views import ShopViewSet, ShopApi, ProductApi, CategoryApi
from rest_framework.routers import DefaultRouter




urlpatterns = [
    # path('', include(router.urls)),
    path('/shops', ShopApi),
    path('/products', ProductApi),
    path('/categories', CategoryApi),
]
from django.urls import include, path
from .views import ShopViewSet, ShopApi, ProductApi, CategoryApi, StaffApi
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('', include(router.urls)),
    path('/shops', ShopApi),
    path('/products', ProductApi),
    path('/categories', CategoryApi),
    path('/staff', StaffApi),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
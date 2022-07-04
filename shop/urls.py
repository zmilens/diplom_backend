from django.urls import include, path
from .views import ShopViewSet, ShopApi, ProductApi, CategoryApi, StaffApi, SaveFile
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('/shops', ShopApi),
    # path('/products/<int:id>', ProductApi),
    path('/products', ProductApi),
    path('/categories', CategoryApi),
    path('/staff', StaffApi),
    path('/file', SaveFile)
]+ static('/'+ settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url(r'api_author/$', views.AuthorsApi),
#     url(r'api_category/$', views.CategoryApi),
#     url(r'api_kitchen/$', views.KitchenApi),
#     url(r'api_author/([0-9]+)$', views.AuthorsApi),
#     url(r'api_recipe/$', views.RecipeApi),
#     url(r'api_recipe/([0-9]+)$', views.RecipeApi),
#     url('', include(router.urls)),
#     url(r'^auth/', CustomAuthToken.as_view(),),
#     url(r'^SaveFile$', SaveFile)
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
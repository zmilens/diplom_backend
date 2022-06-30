from django.http import JsonResponse
from requests import request
from authorization.models import Account
from cart.models import Cart, CartProduct
from cart.serializers import CartProductSerializer, CartSerializer
from shop import serializers

from shop.models import Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
    
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CartApi(request, id=0):
    if request.method == 'GET':
        try:
            cart = Cart.objects.get(owner=request.user)
        except Cart.DoesNotExist:
            cart = None
        serializer_class = CartSerializer(cart)
        return Response( serializer_class.data, status=200)
    # if request.method == 'GET':
    #     # try:
    #     #     cart = Cart.objects.get(owner=request.user)
    #     # except Cart.DoesNotExist:
    #     #     cart = None
    #     cart = Cart.objects.filter(owner=request.user.id).first()
    #     serializer_class = CartSerializer()
    #     print(cart, request.user.id)
    #     return Response( serializer_class.data, status=200)

    # elif request.method == 'POST':
    #     # cart = Cart(request.cart)
    #     # product_data = JSONParser().parse(request)
    #     product = CartProduct.objects.all()
    #     serializer_product = CartProductSerializer(product)
    #     print(serializer_product, product)
    #     if serializer_product.is_valid():
    #         serializer_product.save()
    #         cart.products.add(product_data)
    #         cart.save()
    #         return Response("Товар добавлен в корзину!", serializer_product.data, safe=False)
    #     return Response("not add")


    elif request.method == 'DELETE':
        return JsonResponse("Товар удален из корзины!", safe=False)
    return JsonResponse({'hh': 'hhh'}, status=200)

    # elif request.method=='POST':
    #     product_data=JSONParser().parse(request)
    #     serializer = ProductSerializer(data=product_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse("Товар добавлен успешно!", safe=False)
    #     return JsonResponse("Товар не добавлен.", safe=False)
# class OrderViewSet(ModelViewSet):

#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()
    
#     # @staticmethod
#     # def get_cart(user):
#     #     if user.is_authenticated:
#     #         return Cart.objects.filter(owner=user.customer, for_anonymous_user=False).first()
#     #     return Cart.objects.filter(for_anonymous_user=True).first()

#     # @staticmethod
#     # def _get_or_create_order_product(customer: Account, order: Order, product: Product):
#     #     order_product, created = ProductsInOrder.objects.get_or_create(
#     #         user=customer,
#     #         product=product,
#     #         order=order
#     #     )
#     #     return order_product, created
    
#     # @action(methods=["get"], detail=False)
#     # def current_customer_order(self, *args, **kwargs):
#     #     order = self.get_order(self.request.user)
#     #     order_serializer = OrderSerializer(order)
#     #     return Response(order_serializer.data)

#     # @action(methods=['put'], detail=False, url_path='current_customer_order/add_to_order/(?P<product_id>\d+)')
#     # def product_add_to_order(self, *args, **kwargs):
#     #     order = self.get_order(self.request.user)
#     #     product = get_object_or_404(Product, id=kwargs['product_id'])
#     #     order_product, created = self._get_or_create_order_product(self.request.user.id, order, product)
#     #     if created:
#     #         order.products.add(order_product)
#     #         order.save()
#     #         return Response({"detail": "Товар добавлен в корзину", "added": True})
#     #     return Response({'detail': "Товар уже в корзине", "added": False}, status=status.HTTP_400_BAD_REQUEST)

#     # @action(methods=["patch"], detail=False, url_path='current_customer_order/change_rental_period/(?P<rental_period>\d+)/(?P<order_product_id>\d+)')
#     # def product_change_rental_period(self, *args, **kwargs):
#     #     order_product = get_object_or_404(ProductsInOrder, id=kwargs['order_product_id'])
#     #     order_product.rental_period = int(kwargs['rental_period'])
#     #     order_product.save()
#     #     order_product.order.save()
#     #     return Response(status=status.HTTP_200_OK)


#     # @action(methods=["put"], detail=False, url_path='current_customer_order/remove_from_order/(?P<cproduct_id>\d+)')
#     # def product_remove_from_order(self, *args, **kwargs):
#     #     order = self.get_order(self.request.user)
#     #     cproduct = get_object_or_404(ProductsInOrder, id=kwargs['cproduct_id'])
#     #     order.products.remove(cproduct)
#     #     cproduct.delete()
#     #     order.save()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def order_view(request):
#     if request.user.is_authenticated:
#         order = Order.objects.get(id=request.user.id)
#         return Order.objects.filter(customer=request.user.id).first()
#     return Order.objects.filter(for_anonymous_user=True).first()


# @api_view(['GET'])
# def userdata_view(request):
#     if request.user.is_authenticated:
#         acc = Account.objects.get(id=request.user.id)
#         serializer_account = AccountSerializer(acc)
#         return JsonResponse(serializer_account.data, status=200)
#     return JsonResponse({'message': 'Не авторизован'}, status=401)
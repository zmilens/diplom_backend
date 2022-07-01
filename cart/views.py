from django.http import JsonResponse
from requests import request
from authorization.models import Account
from cart.models import Cart, CartProduct
from cart.serializers import CartProductSerializer, CartSerializer
from shop import serializers
import decimal
from shop.models import Product
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from shop.serializers import ProductSerializer
    
@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def CartApi(request, id=0):
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'Не авторизован'}, status=401)
    acc = Account.objects.get(id=request.user.id)
    #ищу корзину пользователя
    try:
        cart = Cart.objects.get(owner=acc)
    #создаю корзину, если ее нет 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(owner=acc)
        cart.owner=acc
    serializer_cart = CartSerializer(cart)
    if request.method == 'GET':
        serializer_class = CartSerializer(cart)
        return Response( serializer_class.data, status=200)
    elif request.method == 'POST':
        # reqData = { qty: number, productId: number }
        product_data = JSONParser().parse(request)

        try:
            product = Product.objects.get(id=product_data['productId'])
        except:
            return JsonResponse({ 'message': 'Товар не найден'  }, status=400)
        serializer_product = ProductSerializer(product)
        
        try:
            cartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
            serializer_cartProduct = CartProductSerializer(cartProduct)
            CartProduct.objects.filter(product=product_data['productId'], cart=cart).update(qty=serializer_cartProduct.data['qty'] + 
                                                                                product_data['qty'], 
                                                                                final_price=decimal.Decimal(serializer_cartProduct.data['qty']+product_data['qty']) 
                                                                                * decimal.Decimal(serializer_product.data['price']))
        except CartProduct.DoesNotExist:
            cartProduct = CartProduct.objects.create(product=product, cart=cart, qty=product_data['qty'], final_price=product_data['qty']*serializer_product.data['price'], user=acc)
            cart.products.add(cartProduct)

        cart.save()
        return JsonResponse({'message': serializer_cart.data}, status=200)

    elif request.method == 'DELETE':
        # { productId: number }
        product_data = JSONParser().parse(request)
        cart.products.filter(product=product_data['productId']).delete()
        cart.save()
        return JsonResponse({'message': "Товар удален из корзины!"}, safe=False)

    elif request.method == 'PUT':
        # { productId: number, qty: number }
        product_data = JSONParser().parse(request)
        cartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
        product = Product.objects.get(id=product_data['productId'])
        serializer_product = ProductSerializer(product)
        CartProduct.objects.filter(product=product_data['productId'], cart=serializer_cart.data['id']).update(qty=product_data['qty'], final_price=decimal.Decimal(product_data['qty']) * decimal.Decimal(serializer_product.data['price']))
        newCartProduct = CartProduct.objects.get(product=product_data['productId'], cart=cart)
        serializer_cartProduct = CartProductSerializer(newCartProduct)
        cart.save()
        return JsonResponse({'product': serializer_cartProduct.data}, status=200)
        
    return JsonResponse({'message': 'Method not found'}, status=404)


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
from django.db import models
from django.contrib.auth.models import User
from authorization.models import Account
from shop.models import Product, Shop

 
class Order(models.Model):
    customer = models.ForeignKey(Account, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductsInOrder')
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    delivery_address = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    class Status(models.IntegerChoices):
        new = 0, 'Новый'
        in_processing = 1, 'В обработке'
        delivery = 2, 'Передан курьеру'
        completed = 3, 'Завершен'
    status = models.IntegerField(choices=Status.choices, default=Status.new)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество товара в заказе')
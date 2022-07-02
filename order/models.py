from django.db import models
from shop.models import Product, Shop
from authorization.models import Account

class ProductsInOrder(models.Model):
    customer = models.OneToOneField(Account, verbose_name='Покупатель', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ', related_name='related_order')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')


class Order(models.Model):
    customer = models.ForeignKey(Account, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(ProductsInOrder, verbose_name='Товары', blank=True, related_name='related_products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    class Status(models.IntegerChoices):
        new = 0, 'Новый'
        in_processing = 1, 'В обработке'
        delivery = 2, 'Подтвержден'
        completed = 3, 'Завершен'
    status = models.IntegerField(choices=Status.choices, default=Status.new)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


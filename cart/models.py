from itertools import product
from django.db import models
from django.contrib.auth.models import User
from authorization.models import Account
from shop.models import Product, Shop

class CartProduct(models.Model):
    user = models.ForeignKey(Account, verbose_name='Покупатель', on_delete=models.CASCADE)
    # cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey(Account, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            self.total_products = self.products.count()
            self.final_price = sum([cproduct.final_price for cproduct in self.products.all()])
        super().save(*args, **kwargs)


class Order(models.Model):
    customer = models.ForeignKey(Account, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductsInOrder')
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

class ProductsInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар', related_name='count_in_order',)
    rental_period = models.PositiveSmallIntegerField(verbose_name='Срок аренды')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')


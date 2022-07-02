from django.db import models
from authorization.models import Account
from shop.models import Product, Shop
# Create your models here.
class OrderProduct(models.Model):
    user = models.ForeignKey(Account, verbose_name='Покупатель', on_delete=models.CASCADE)
    order = models.ForeignKey('Order', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    qty = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')





class Order(models.Model):
    owner = models.ForeignKey(Account, verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct, blank=True, related_name='related_order')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name='Магазин', related_name="order_shop")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    
    class Status(models.IntegerChoices):
        new = 0, 'Новый'
        in_processing = 1, 'В обработке'
        delivery = 2, 'Подтвержден'
        completed = 3, 'Завершен'
    status = models.IntegerField(choices=Status.choices, default=Status.new)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.id:
            self.total_products = self.products.count()
            self.final_price = sum([cproduct.final_price for cproduct in self.products.all()])
        super().save(*args, **kwargs)
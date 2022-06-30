from django.db import models

from django.contrib.auth.models import User

from authorization.models import Account

class Shop(models.Model):
    title = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    owner = models.OneToOneField(Account, on_delete=models.PROTECT) 

    class Meta:
        ordering = ('title',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.title

class Staff(models.Model):
    operator = models.OneToOneField(Account, on_delete=models.PROTECT) 
    shop = models.ForeignKey(Shop, related_name='shop_id', on_delete=models.PROTECT)
    class Meta:
        ordering = ('operator',)
        verbose_name = 'Оператор'
        verbose_name_plural = 'Операторы'

class Category(models.Model):
    title = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(max_length=255, upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    shop = models.ForeignKey(Shop, related_name='shop', on_delete=models.PROTECT)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name




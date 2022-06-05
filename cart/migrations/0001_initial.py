# Generated by Django 4.0.4 on 2022-06-03 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('status', models.IntegerField(choices=[(0, 'Новый'), (1, 'В обработке'), (2, 'Передан курьеру'), (3, 'Завершен')], default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ProductsInOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Количество товара в заказе')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='count_in_order', to='shop.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, through='cart.ProductsInOrder', to='shop.product', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='order',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop', verbose_name='Магазин'),
        ),
    ]
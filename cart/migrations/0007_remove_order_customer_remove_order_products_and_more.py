# Generated by Django 4.0.4 on 2022-07-01 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_cart_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shop',
        ),
    ]
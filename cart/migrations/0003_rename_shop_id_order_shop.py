# Generated by Django 4.0.4 on 2022-06-07 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_order_delivery_address_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shop_id',
            new_name='shop',
        ),
    ]
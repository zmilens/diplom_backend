# Generated by Django 4.0.4 on 2022-06-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ('operator',), 'verbose_name': 'Оператор', 'verbose_name_plural': 'Операторы'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='products/%Y/%m/%d'),
        ),
    ]
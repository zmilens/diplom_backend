from django.contrib import admin
from .models import Shop, Category, Product, Staff
from import_export.admin import ImportExportModelAdmin

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ('title', 'city', 'address')
    ordering = ['title']
    pass

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    list_display = ('operator', 'shop')
    ordering = ['operator']
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('title', )
    ordering = ['title']
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price', 'stock', 'available', 'created', 'updated', 'shop_id')
    ordering = ['name', 'category']
    pass
from django.contrib import admin
from .models import Shop, Category, Product
from import_export.admin import ImportExportModelAdmin

@admin.register(Shop)
class ShopAdmin(ImportExportModelAdmin):
    list_display = ('title', 'city', 'address')
    ordering = ['title']
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('title', )
    ordering = ['title']
    prepopulated_fields = {'slug': ('title',)}
    pass

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'description', 'price', 'stock', 'available', 'created', 'updated', 'shop_id')
    ordering = ['name', 'category']
    prepopulated_fields = {'slug': ('name',)}
    pass
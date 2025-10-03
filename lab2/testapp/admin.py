from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")  # показуємо ID і назву категорії
    search_fields = ("name",)       # пошук за назвою категорії

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")  # показуємо ключові поля
    list_filter = ("category",)                        # фільтрація за категоріями
    search_fields = ("name", "category__name")         # пошук за назвою продукту або категорії
    ordering = ("name",)                               # сортування за назвою

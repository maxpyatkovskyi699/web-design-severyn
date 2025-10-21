from django.contrib import admin
from .models import Category, Product

# Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')      # Додаємо slug до відображення
    list_editable = ('name',)                  
    list_filter = ('name',)                    
    search_fields = ('name', 'slug')           # Додаємо slug до пошуку
    ordering = ('name',)                       
    # Автоматичне заповнення slug на основі name
    prepopulated_fields = {'slug': ('name',)}

# Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'description', 'slug') # Додаємо slug
    list_editable = ('price', 'category', 'description')                      
    list_filter = ('category', 'price')                                       
    search_fields = ('name', 'description', 'slug')                           # Додаємо slug до пошуку
    ordering = ('name',)                                                      
    # Автоматичне заповнення slug на основі name
    prepopulated_fields = {'slug': ('name',)}
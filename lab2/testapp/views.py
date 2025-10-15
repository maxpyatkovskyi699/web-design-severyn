from django.shortcuts import render
from .models import Category, Product  # якщо є моделі

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'testapp/index.html', {
        'categories': categories,
        'products': products
    })

# Обробник для списку категорій
def category_list(request):
    categories = Category.objects.all()  # Отримуємо всі категорії з БД
    return render(request, "testapp/category_list.html", {"categories": categories})


# Обробник для списку продуктів
def product_list(request):
    products = Product.objects.all()  # Отримуємо всі продукти з БД
    return render(request, "testapp/product_list.html", {"products": products})
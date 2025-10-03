from django.shortcuts import render
from .models import Category, Product  # якщо є моделі

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'testapp/index.html', {
        'categories': categories,
        'products': products
    })

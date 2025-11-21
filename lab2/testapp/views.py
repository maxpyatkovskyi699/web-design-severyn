from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.utils.text import slugify

# Головна сторінка
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'testapp/index.html', {
        'categories': categories,
        'products': products
    })

# Списки з пагінацією
def category_list(request):
    categories = Category.objects.all().order_by('id')
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'testapp/category_list.html', {'page_obj': page_obj})

def product_list(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'testapp/product_list.html', {'page_obj': page_obj})

# CRUD для Category
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            if not category.slug:
                category.slug = slugify(category.name)
            category.save()
            return redirect('category_detail', slug=category.slug)
    else:
        form = CategoryForm()
    return render(request, 'testapp/category_form.html', {'form': form})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'testapp/category_detail.html', {
        'category': category,
        'products': products
    })

def category_update(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            if not category.slug:
                category.slug = slugify(category.name)
            category.save()
            return redirect('category_list', slug=category.slug)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'testapp/category_form.html', {'form': form})

def category_delete(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'testapp/category_confirm_delete.html', {'category': category})

# CRUD для Product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            if not product.slug:
                product.slug = slugify(product.name)
            product.save()
            return redirect('product_detail', slug=product.slug)
    else:
        form = ProductForm()
    return render(request, 'testapp/product_form.html', {'form': form})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'testapp/product_detail.html', {'product': product})

def product_update(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            if not product.slug:
                product.slug = slugify(product.name)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'testapp/product_form.html', {'form': form})

def product_delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'testapp/product_confirm_delete.html', {'product': product})

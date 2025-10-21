from django.urls import path
from django.utils.text import slugify
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Категорії
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'), 
    path('categories/<slug:slug>/update/', views.category_update, name='category_update'),
    path('categories/<slug:slug>/delete/', views.category_delete, name='category_delete'),

    # Продукти
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'), 
    path('products/<slug:slug>/update/', views.product_update, name='product_update'),
    path('products/<slug:slug>/delete/', views.product_delete, name='product_delete'),
]

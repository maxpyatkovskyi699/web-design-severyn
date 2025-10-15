from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # головна сторінка
    path('categories/', views.category_list, name='category_list'),  # сторінка категорій
    path('products/', views.product_list, name='product_list'),      # сторінка продуктів
]

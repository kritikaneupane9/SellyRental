from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('form/', views.product_create, name='product_form'),
    path('form/<int:pk>/', views.product_update, name='product_form'),
    path('delete/<int:pk>/', views.product_delete, name='product_confirm_delete'),
    path('shop/', views.customer_product_list, name='customer_products_list')
]


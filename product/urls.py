from django.urls import path, include
from . import views
from bid.views import bid_create
app_name = 'product'

urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('form/', views.product_create, name='product_form'),
    path('form/<int:pk>/', views.product_update, name='product_form'),
    path('delete/<int:pk>/', views.product_delete, name='product_confirm_delete'),


    path('customer/product/', views.customer_product_list, name='customer_products'),
    path('product/<int:pk>/', views.customer_product_detail, name='product_detail'),
    path('product/<int:product_id>/action/', views.customer_product_action, name='product_action'),
    path('product/<int:pk>/bid/', bid_create, name='bid_create'),

]


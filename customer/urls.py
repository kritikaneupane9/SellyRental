from django.urls import path
from customer import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('update/<int:pk>/', views.customer_update, name='customer_edit'),
    path('delete/<int:pk>/', views.customer_delete, name='customer_delete'),
    path('products/', views.customer_product_list, name='customer_product_list'),
    path('product/<int:pk>/',views.customer_product_list,name='customer_product'),
    path('', views.home, name='home'),
]





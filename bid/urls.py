from django.urls import path
from . import views

urlpatterns = [

    path('', views.bid_list, name='bid_list_all'),

    path('product/<int:product_id>/', views.bid_list, name='bid_list'),

    path('form/<int:product_id>/', views.bid_create, name='bid_create'),

    path('delete/<int:pk>/', views.bid_confirm_delete, name='bid_confirm_delete'),
]

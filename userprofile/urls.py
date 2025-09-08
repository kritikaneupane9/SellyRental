from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('', views.profile_home, name='profile'),
    path('account/', views.account_detail, name='account_detail'),
    path('orders/', views.order_history, name='order_history'),
    path('logout/', views.logout_user, name='logout_user'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.order_history, name='order_history'),
]

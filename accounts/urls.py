from django.urls import path
from. import views
from accounts.views import register_views, login_views, logout_views

urlpatterns = [
    path('', views.login_views, name='accounts-home'),
    path('register/', views.register_views, name='register'),
    path('login/', views.login_views, name='login'),

]
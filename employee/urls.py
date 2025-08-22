from django.urls import path
from employee import views

app_name = 'employee'
urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('create/',views.employee_create, name="employee_create"),
    path('update/<int:pk>/', views.employee_update, name='employee_edit'),
    path('delete/<int:pk>/', views.employee_delete, name='employee_delete'),
]
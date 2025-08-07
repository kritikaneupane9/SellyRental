from django.urls import path
from customer import views

urlpatterns = [

    path("list", views.customer_list, name="customer_list"),



]

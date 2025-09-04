from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from product.models import Product


def cart_add(request, product_id):
    cart = Cart(request) #it initializes the cart from this session
    product = get_object_or_404(Product, id=product_id)
    cart.add(product, quantity=1)
    messages.success(request,"Added to cart.")
    return redirect('product:product_detail', pk=product_id)

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    context ={'cart':cart}
    return render(request, 'home/cart_detail.html',context)


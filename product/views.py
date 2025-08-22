from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


# List all products
def product_list(request):
    products = Product.objects.all().annotate(highest_bid=Max('bids__amount'))
    return render(request, 'product/product_list.html', {'products': products})


# Add product
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, 'product/product_form.html', context)


# Update product
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        # include request.FILES here as well
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    context = {'form': form}
    return render(request, 'product/product_form.html', context)


# Delete product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    context = {'product': product}
    return render(request, 'product/product_confirm_delete.html', context)

def customer_product_list(request):
    products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'customer/customer_product_list.html',context)
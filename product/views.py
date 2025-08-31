from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Category
from .forms import ProductForm, ProductFilterForm


def product_list(request):
    products = Product.objects.all().annotate(highest_bid=Max('bids__amount'))
    categories = Category.objects.all()
    return render(request, 'product/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'product/product_form.html', context)


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    categories = Category.objects.all()
    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'product/product_form.html', context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    context = {'product': product}
    return render(request, 'product/product_confirm_delete.html', context)


def customer_product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get("category", "")

    if selected_category:
        products = products.filter(category_id=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'customer/customer_product_list.html', context)


def customer_product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'customer/customer_product_detail.html', context)


def customer_product_action(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        print(f"User selected {quantity} of {product.product_name}")
        return redirect('customer_product', pk=product.id)
    return redirect('customer_product', pk=product.id)

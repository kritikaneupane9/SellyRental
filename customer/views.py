from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import RegisterForm, LoginForm
from customer.models import Customer
from product.models import Product, Category


def customer_list(request):
    customers = Customer.objects.all()
    context ={
        'customers': customers
    }
    return render(request, 'customer/customer_list.html', context)

def customer_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        '''        Customer.objects.create(
            name=name,
            address=address, 
            phone_number=phone_number)'''
        customer = Customer()
        customer.name = name
        customer.address = address
        customer.phone_number = phone_number
        customer.save()


        return redirect('customer_list')
    return render(request, 'customer/customer_create.html')

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk) #404 is a shortcut

    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.address = request.POST.get('address')
        customer.phone_number = request.POST.get('phone_number')
        customer.save()
        return redirect('customer_list')

    return render(request, 'customer/customer_edit.html', {'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'customer/customer_delete.html', {'customer': customer})
def customer_product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get("category", "")
    search_query = request.GET.get("q", "")
    if selected_category:
        products = products.filter(category_id=selected_category)
    if search_query:
        products = products.filter(product_name__icontains=search_query)
    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
    }

    return render(request, 'customer/customer_product_list.html', context)

def customer_product_detail(request,pk):
    product = get_object_or_404(Product, pk=pk)
    context ={'product':product}
    return render(request, 'customer/customer_product_detail.html',context)

def home(request):
    top_bid_products = Product.objects.annotate(
        highest_bid = Max('bids__amount')
    ).order_by('-highest_bid')[:5]
    context ={
        'top_bid_products': top_bid_products
    }
    return render(request, 'home/home.html', context)

def register_views(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})


def login_views(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_views(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

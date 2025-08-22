from django.shortcuts import render, redirect, get_object_or_404
from customer.models import Customer
from product.models import Product


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
    #
    return render(request, 'customer/customer_edit.html', {'customer': customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')

    return render(request, 'customer/customer_delete.html', {'customer': customer})

def customer_product_list(request):
    product = Product.objects.all()
    context ={'product':product}
    return render(request,'customer/customer_product_list.html',context)

def home(request):
    return render(request, 'home/home.html')
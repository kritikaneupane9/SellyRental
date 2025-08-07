from django.shortcuts import render

from customer.models import Customer


# Create your views here.
def customer_list(request):
    # This function will render the customer list page.
    customer = Customer.objects.all()
    context = {
        'customer' :customer

    }
    return render(request, 'Customer/customer_list.html', context)

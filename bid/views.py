from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Bid
def bid_list(request, product_id=None):
    if product_id:
        bids = Bid.objects.filter(product_id=product_id)\
            .annotate(highest_bid=Max('product__bids__amount'))\
            .order_by('-amount', 'id')
    else:
        bids = Bid.objects.all()\
            .annotate(highest_bid=Max('product__bids__amount'))\
            .order_by('-amount', 'id')
    context = {'bids': bids}
    return render(request, 'bid/bid_list.html', context)

def bid_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        bidder_name = request.POST.get("bidder_name")
        amount = request.POST.get("amount")
        Bid.objects.create(
            product=product,
            bidder_name=bidder_name,
            amount=amount
        )
        return redirect('customer_product_detail',pk=product.pk)
    return render(request, 'bid/bid_form.html', {'product': product})

def bid_confirm_delete(request,pk):
    bid = get_object_or_404(Bid, pk=pk)
    if request.method =="POST":
        bid.delete()
        return redirect('bid_list',product_id=bid.product.id)
    context ={
        'bid':bid
    }
    return render(request, 'bid/bid_confirm_delete.html',context)


#POST - User clicked submit - save bid - go to list
#GET - user open form - show empty


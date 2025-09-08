from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from cart.cart import Cart
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Order
from .models import Profile

@login_required
def profile_home(request):
    return render(request, 'userprofile/profile.html')

@login_required
def account_detail(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('userprofile:account_detail')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'userprofile/account_detail.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'userprofile/order_history.html', {'orders': orders})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def checkout(request):
    cart = Cart(request)

    if len(cart) == 0:
        return redirect('cart:view')  # adjust cart view name

    # create orders
    for item in cart:
        Order.objects.create(
            user=request.user,
            product=item['product'],
            quantity=item['quantity'],
            total_price=item['subtotal']
        )

    # clear cart
    cart.clear()

    return redirect('userprofile:order_history')
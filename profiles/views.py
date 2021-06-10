from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

from django.contrib import messages
from checkout.models import Order

def profile(request):
    '''
    Display user profile
    '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.POST:
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, 'Profile successfully updated!')
        else:
            messages.error(request, 'Profile update is Failed')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page':True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f'This is  past confirmation for order number {order_number}.' 
    'A confirmation was sent on the order date'))

    template = 'checkout/checkout_success.html'
    context = {
        'order':order,
        'from_profile': True,
    }

    return render(request, template, context)
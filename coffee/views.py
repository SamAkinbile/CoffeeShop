# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Coffee

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def checkout(request):
    cart_items = CartItem.objects.all()
    total = sum(item.coffee.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})

def add_to_cart(request, coffee_id):
    coffee = get_object_or_404(Coffee, id=coffee_id)
    cart_item, created = CartItem.objects.get_or_create(coffee=coffee)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('home')

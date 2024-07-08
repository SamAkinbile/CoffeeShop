from django.shortcuts import render
from .models import Coffee

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})

def checkout(request):
    coffee = Coffee.objects.all()
    return render(request, 'checkout.html', {'coffee': coffee})

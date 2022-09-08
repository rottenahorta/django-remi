from django.shortcuts import render

# Create your views here.

from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def index(request):
    products = Product.objects.all()
    return render(request, 'remi/index.html', {'products':products})

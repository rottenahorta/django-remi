from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Category, Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def index(request):
    products = Product.objects.all()
    return render(request, 'remi/index.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True) # q to db
    return render(request, 'remi/products/detail.html', {'product':product})

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'remi/products/category.html', {'category':category, 'products':products})

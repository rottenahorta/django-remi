from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from remi.models import Product
# Create your views here.

def basket(request):
    return {'basket': Basket(request)}

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = request.POST.get('product_quantity')
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_quantity=product_quantity)
        response = JsonResponse({'quantity':basket.__len__()})
        return response

def basket_index(request):
    return render(request, 'remi/basket/index.html')
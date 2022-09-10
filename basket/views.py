from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from remi.models import Product
# Create your views here.

def basket(request):
    return {'basket': Basket(request)}

def basket_action(request):
    basket = Basket(request)
    pid = int(request.POST.get('product_id'))
    if request.POST.get('action') == 'add':
        product = get_object_or_404(Product, id=pid)
        product_quantity = request.POST.get('product_quantity')
        basket.add(product=product, product_quantity=product_quantity)
        response = JsonResponse({'quantity':basket.__len__()})
    if request.POST.get('action') == 'delete':
        pid = str(pid)
        basket.delete(pid=pid)
        tp = str(basket.get_total_price())
        q = basket.__len__()
        response = JsonResponse({'product_id':pid, 'total_price':tp, 'quantity':q})
    return response

def basket_index(request):
    return render(request, 'remi/basket/index.html')
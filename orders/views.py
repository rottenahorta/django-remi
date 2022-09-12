from django.shortcuts import render

from .models import Order, OrderProduct
from basket.basket import Basket
# Create your views here.

def orders_success(request):
    basket = Basket(request)
    order = Order.objects.create()
    oid = order.pk
    for product in basket:
        OrderProduct.objects.create(order_id=oid, product=product['product'], price=product['price'], quantity=product['quantity'])
    basket.clear()
    return render(request, 'remi/orders/success.html')
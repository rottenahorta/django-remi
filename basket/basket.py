from decimal import Decimal
from remi.models import Product


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}
        self.basket = basket

    def add(self, product, product_quantity):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] += int(product_quantity) 
        else:
            self.basket[product_id] = {'price': str(product.price), 'quantity': int(product_quantity)}
        self.save()

    def delete(self, pid):
        if pid in self.basket:
            del self.basket[pid]
        self.save()

    def clear(self):
        del self.session['session_key']
        self.save()

    def save(self):
        self.session.modified = True
    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.basket.values())

    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def __iter__(self):
        pid = self.basket.keys()
        products = Product.products.filter(id__in=pid)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

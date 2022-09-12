from django.db import models

# Create your models here.

from remi.models import Product

class Sale(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return str(self.name)

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sale")

    #def get_price_sale(self,obj):
    #    return obj.product.price_sale

    def __str__(self):
        return str(self.product.title)

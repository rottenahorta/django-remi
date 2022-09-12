from django.shortcuts import render, get_object_or_404

from .models import Sale, SaleProduct

def sales(request):
    return {
        'sales': Sale.objects.all()
    }

def sales_index(request):
    return render(request, "remi/sales/index.html")

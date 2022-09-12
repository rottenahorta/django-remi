from django.contrib import admin

from .models import Order, OrderProduct
# Register your models here.

class OrderInlines(admin.TabularInline):
    model = OrderProduct

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderInlines,)
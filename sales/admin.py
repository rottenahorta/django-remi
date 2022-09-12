from django.contrib import admin

from .models import Sale, SaleProduct

class SaleProductInlines(admin.TabularInline):
    model = SaleProduct
    #fields = (...,'get_price_sale')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    inlines = [
        SaleProductInlines,
    ]
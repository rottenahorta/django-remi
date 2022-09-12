from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, ProductSpecification, ProductSpecificationValue, ProductType

# Register your models here.

from .models import Category, Product

@admin.register(Category)
class Category(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]

class ProductSpecificationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        ProductSpecificationValueInline,
    ]
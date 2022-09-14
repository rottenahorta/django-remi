from remi.models import Category, Product, ProductSpecificationValue
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        read_only = True

class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        depth = 2
        exclude = ['id', 'product']
        read_only = True

class ProductSerializer(serializers.ModelSerializer):
    specification = ProductSpecificationValueSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        depth = 2
        fields = ['title', 'slug', 'brand', 'is_active', 'price', 'price_sale', 'specification']
        read_only = True

class ProductSearchSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        depth = 2
        fields = ['title', 'brand', 'category']
        read_only = True
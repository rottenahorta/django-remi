from rest_framework.views import APIView
from rest_framework.response import Response
from remi.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer, ProductSearchSerializer

class CategoryList(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class ProductsByCategory(APIView):
    def get(self, request, category_slug=None):
        queryset = Product.objects.filter(category__slug=category_slug)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductBySlug(APIView):
    def get(self, request, product_slug=None):
        queryset = Product.objects.filter(slug=product_slug)
        serializer = ProductSerializer(queryset, many=True) # bug w/o many
        return Response(serializer.data)

class ProductSearch(APIView):
    def get(self, request, product_slug=None):
        queryset = Product.objects.filter(slug=product_slug)
        serializer = ProductSearchSerializer(queryset, many=True)
        return Response(serializer.data)
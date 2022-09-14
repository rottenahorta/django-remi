from django.urls import path

from search.views import SearchProduct
from .views import CategoryList, ProductSearch, ProductsByCategory, ProductBySlug

app_name = 'drf'
urlpatterns = [
    path('categories', CategoryList.as_view()),
    path('products/category/<str:category_slug>', ProductsByCategory.as_view()),
    path('products/<str:product_slug>', ProductBySlug.as_view()),
    path('search/<str:query>', SearchProduct.as_view()),
    path('searchtmp/<str:product_slug>', ProductSearch.as_view()),
]

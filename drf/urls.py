from django.urls import path
from .views import CategoryList, ProductByCategory

app_name = 'drf'
urlpatterns = [
    path('category', CategoryList.as_view()),
    path('products/category/<str:category_slug>', ProductByCategory.as_view()),
]

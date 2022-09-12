from django.urls import path
from . import views

app_name = 'remi' #namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
    path('category/<slug:slug>', views.category_list, name='category_list'),
]

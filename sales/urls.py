from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
    path('', views.sales_index, name='sales_index')
]
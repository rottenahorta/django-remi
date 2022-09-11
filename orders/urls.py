from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('success/', views.orders_success, name='orders_success')
]
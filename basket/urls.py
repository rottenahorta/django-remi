from django.urls import path

from . import views

app_name = 'basket'
urlpatterns = [
    path('', views.basket_index, name='basket_index'),
    path('action/', views.basket_action, name='basket_action')
]
from django.urls import path
from . import views

app_name = 'remi' #namespace
urlpatterns = [
    path('', views.index, name='index')
]

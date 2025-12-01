from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
]

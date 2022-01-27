from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cafes/', views.cafes, name="cafes"),
    path('add/', views.add_new, name="add"),
]
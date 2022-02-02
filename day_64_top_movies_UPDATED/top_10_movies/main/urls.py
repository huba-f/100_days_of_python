from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('update-movie/<movie_id>', views.update_movie, name="update_movie"),
    path('delete-movie/<movie_id>', views.delete_movie, name="delete_movie"),
]



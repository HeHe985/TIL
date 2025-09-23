from django.urls import path
from libraries import views

urlpatterns = [
    path('', views.index, name='index'),
    path('libraries/recommend/', views.recommend, name='recommend'),
    path('libraries/bestseller/', views.bestseller, name='bestseller'),
]

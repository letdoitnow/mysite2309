from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gioi-thieu/', views.about),
]

from django.urls import path
from . import views

urlpatterns = [
    path('danh-sach/', views.list),
    path('chi-tiet/', views.detail),
]

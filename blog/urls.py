from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('detail/', views.blog_detail),
]

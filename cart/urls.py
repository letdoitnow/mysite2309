from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('', views.cart, name="cart"),
    path('order/<int:id>/', views.order, name="order"),
    path('add_to_cart/<int:id>/', views.add_to_cart, name="add_to_cart"),
]

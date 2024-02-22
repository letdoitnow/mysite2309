from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('', views.cart, name="cart"),
    path('order/<int:id>/', views.order, name="order"),
]

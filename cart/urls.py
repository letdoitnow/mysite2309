from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('', views.cart, name="cart"),
    path('<int:id>/', views.buy_now, name="buy_now"),
    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('order/<int:id>/', views.order, name="order"),
]

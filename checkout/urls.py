from django.urls import path
from . import views

app_name = "checkout"
urlpatterns = [
    path('<int:id>/', views.checkout, name="checkout"),
]

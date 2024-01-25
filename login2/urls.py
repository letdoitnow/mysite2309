from django.urls import path
from . import views

app_name = "login2"
urlpatterns = [
    path('', views.login2, name="login2"),
]

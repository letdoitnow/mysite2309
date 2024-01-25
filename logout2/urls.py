from django.urls import path
from . import views

app_name = "logout2"
urlpatterns = [
    path('', views.logout2, name="logout2"),
]

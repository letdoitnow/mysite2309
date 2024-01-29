from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('api/', views.todos_list, name="todos_list"),
    path('<int:id>/api/', views.todos_detail, name="todos_detail"),
]

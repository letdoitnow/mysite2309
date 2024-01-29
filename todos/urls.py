from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('', views.todos_list, name="todos_list"),
    path('api/', views.todos_list_api, name="todos_list_api"),
    path('<int:id>/api/', views.todos_detail_api, name="todos_detail_api"),
]

from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('', views.student_list, name="student_list"),
    path('<int:id>/', views.student_detail, name="student_detail"),
    path('them-moi/', views.student_add, name="student_add"),
]

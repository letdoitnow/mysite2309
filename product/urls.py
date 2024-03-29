from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('chi-tiet/<int:id>/', views.product_detail, name="product_detail"),
    path('them-moi/', views.product_add, name='product_add'),
    path('cap-nhat/<int:id>/', views.product_edit, name='product_edit'),
    path('xoa/<int:id>/', views.product_delete, name='product_delete'),
]

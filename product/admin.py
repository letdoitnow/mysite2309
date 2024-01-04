from django.contrib import admin
from .models import ProductModel

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "quantity"]
    list_filter = ["created_at"]
    search_fields = ["product_name"]

# Register your models here.
admin.site.register(ProductModel, ProductAdmin)

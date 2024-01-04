from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel

# Create your views here.
def product_list(request):
    # return HttpResponse("Product list")
    product_list = ProductModel.objects.all().order_by("-created_at")

    context = {
        "product_list": product_list
    }

    return render(request, "product/product_list.html", context)

def product_detail(request, id):
    # return HttpResponse("Product detail")
    product = ProductModel.objects.get(pk=id)
    context = {
        "product": product
    }
    return render(request, "product/product_detail.html", context)
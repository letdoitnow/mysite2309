from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel
from django.db.models import Q

# Create your views here.
def product_list(request):
    # return HttpResponse("Product list")
    product_list = ProductModel.objects.all().order_by("-created_at")

    # product_list = ProductModel.objects.filter(
    #     product_name="xiaomi 10", 
    #     delete_flg=False, 
    #     quantity=100,
    #     )
    
    # product_list = ProductModel.objects.filter(product_name="xiaomi 10") | ProductModel.objects.filter(delete_flg=False)
    
    # product_list = ProductModel.objects.filter( Q(product_name="xiaomi 10") | Q(delete_flg=False) )

    # product_list = ProductModel.objects.filter(product_name__contains="i")
    # SELECT * FROM ProductModel WHERE product_name LIKE '%xiaomi%'
    
    #1 lay cac san pham chua chu 'xi' va chu 'sam' ?
    # product_list = ProductModel.objects.filter(Q(product_name__contains="xi") & Q(product_name__contains="sam"))

    #2 lay cac san pham chua chu 'xi' hoac chu 'sam' ?
    # product_list = ProductModel.objects.filter(Q(product_name__contains="xi") | Q(product_name__contains="sam"))

    # product_list = ProductModel.objects.filter(created_at__year__gte=2024)

    #3 lay cac san pham ma ngay tao >=2023 va so luong > 10
    # product_list = ProductModel.objects.filter(created_at__year__gte=2023, quantity__gt=10)
    # product_list = ProductModel.objects.filter( Q(created_at__year__gte=2023) & Q(quantity__gt=10) )

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
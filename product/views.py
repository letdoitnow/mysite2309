from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel
from django.db.models import Q

# Create your views here.
def product_list(request):
    keyword = request.GET.get("keyword")
    if not keyword:
        product_list = ProductModel.objects.all()
    else:
        product_list = ProductModel.objects.filter(
            Q(product_name__contains=keyword)
            | Q(summary__contains=keyword)
            | Q(description__contains=keyword)
        )

    product_list = product_list.order_by("-created_at")

    context = {
        "product_list": product_list,
        "keyword": keyword if keyword else "",
    }

    return render(request, "product/product_list.html", context)

def product_detail(request, id):
    # return HttpResponse("Product detail")
    product = ProductModel.objects.get(pk=id)
    context = {
        "product": product
    }
    return render(request, "product/product_detail.html", context)
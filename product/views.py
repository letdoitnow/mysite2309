from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product_list(request):
    # return HttpResponse("Product list")
    context = {
        'product_list': [
            {
                "id": 1,
                "product_name": "tivi samsung",
                "price": 20000000,
            },
            {
                "id": 2,
                "product_name": "tivi xiaomi",
                "price": 15000000,
            },
        ]
    }

    return render(request, "product/product_list.html", context)

def product_detail(request, id):
    # return HttpResponse("Product detail")
    context = {
        "id": id,
        "product_name": "tivi samsung",
        "price": 20000000,
        "description": "tivi han quoc",
    }
    return render(request, "product/product_detail.html", context)
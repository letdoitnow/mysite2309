from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductModel
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ProductForm

# Create your views here.
def product_list(request):
    # keyword
    keyword = request.GET.get("keyword")
    if not keyword:
        product_list = ProductModel.objects.all()
    else:
        product_list = ProductModel.objects.filter(
            Q(product_name__contains=keyword)
            | Q(summary__contains=keyword)
            | Q(description__contains=keyword)
        )

    # sort
    sort = request.GET.get("sort")
    if sort not in ["-created_at", "created_at", "price", "-price"]:
        sort = settings.DEFAULT_SORT

    product_list = product_list.order_by(sort)

    # limit
    limit = request.GET.get("limit")
    if limit not in ["2", "5", "10"]:
        limit = settings.DEFAULT_LIMIT
    limit = int(limit)

    # product_list = product_list[:limit]

    # paging
    page = request.GET.get("page")
    product_list_paginator = Paginator(product_list, limit)

    try:
        product_list_paging = product_list_paginator.page(page)
    except PageNotAnInteger:
        product_list_paging = product_list_paginator.page(1)
    except EmptyPage:
        product_list_paging = product_list_paginator.page(product_list_paginator.num_pages)

    context = {
        "product_list": product_list_paging,
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

def product_add(request):
    form = ProductForm()
    context = {
        "form": form
    }
    return render(request, 'product/product_add.html', context)
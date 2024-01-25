from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ProductModel
from django.db.models import Q
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ProductForm, ProductModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
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
    form = ProductModelForm()

    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product:product_list")

    context = {
        "form": form
    }
    return render(request, 'product/product_add.html', context)

def product_edit(request, id):
    model = ProductModel.objects.get(pk=id)
    form = ProductModelForm(instance=model)

    if request.method == "POST":
        form = ProductModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect("product:product_detail", id)

    context = {
        "form": form
    }
    return render(request, 'product/product_edit.html', context)


def product_delete(request, id):
    model = ProductModel.objects.get(pk=id)
    model.delete()
    return redirect("product:product_list")
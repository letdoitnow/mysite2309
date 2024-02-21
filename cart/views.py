from django.shortcuts import render, get_object_or_404, redirect
from product.models import ProductModel
from customer.models import CustomerModel
from orders.models import OrdersModel
from orders_detail.models import OrdersDetailModel
import json
from django.http import JsonResponse
from django.db.models import Avg, Count, Sum
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def cart(request):
    customer = get_object_or_404(CustomerModel, user=request.user)
    order = OrdersModel.objects.filter( 
        status=0,
        customer = customer
    ).first()
    order_detail = OrdersDetailModel.objects.filter(order=order)

    context = {
        'customer': customer,
        'order': order,
        'order_detail': order_detail,
        'cart': get_total_number_item_in_cart(request),
    }
    return render(request, 'cart/cart.html', context)

@login_required(login_url=settings.LOGIN_URL)
def buy_now(request, id):
    add_to_cart_common(request, id)
    return redirect("cart:cart")

@login_required(login_url=settings.LOGIN_URL)
def add_to_cart_common(request, id):
    product = ProductModel.objects.get(id=id)
    customer = CustomerModel.objects.get(user=request.user)

    # orders
    order, created = OrdersModel.objects.get_or_create(
        status=0,
        customer=customer
    )

    # orders_detail
    try:
        orders_detail = OrdersDetailModel.objects.get(
            order=order, 
            product=product,
        )
    except OrdersDetailModel.DoesNotExist:
        orders_detail = OrdersDetailModel(
            order=order, 
            product=product,
            price=product.price,
            quantity=0,
        )
    
    orders_detail.quantity = orders_detail.quantity + 1 if orders_detail.quantity else 1
    orders_detail.price = product.price
    orders_detail.save()

@login_required(login_url=settings.LOGIN_URL)
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["itemId"]
    print(data)
    add_to_cart_common(request, product_id)
    return JsonResponse({"total": get_total_number_item_in_cart(request)})

@login_required(login_url=settings.LOGIN_URL)
def get_total_number_item_in_cart(request):
    customer = CustomerModel.objects.get(user=request.user)
    order = OrdersModel.objects.filter( 
        status=0,
        customer = customer
    ).first()
    total_items = OrdersDetailModel.objects.filter(order=order).aggregate(Sum('quantity'))
    total_items = list(total_items.values())[0]
    return total_items

@login_required(login_url=settings.LOGIN_URL)
def order(request, id):
    # update order item: price
    # update order status
    order = OrdersModel.objects.get(pk=id, status=0)
    order.status = 1
    order.description = request.POST.get("description")

    order_detail = OrdersDetailModel.objects.filter(order=order)
    for item in order_detail:
        item.price = item.product.price
        item.save()
    order.save()

    context = {
        "order": order
    }
    return render(request, "cart/order.html", context)
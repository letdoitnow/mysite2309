from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from customer.models import CustomerModel
from orders.models import OrdersModel
from orders_detail.models import OrdersDetailModel
from product.models import ProductModel


# Create your views here.
def cart(request):
    customer = CustomerModel.objects.get(user=request.user)

    # order - 0 - draft
    order = OrdersModel.objects.filter(
        customer = customer,
        status = 0
    ).first()

    # order detail
    order_detail = OrdersDetailModel.objects.filter(orders=order)


    context = {
        "customer": customer,
        "order": order,
        "order_detail": order_detail,
    }
    return render(request, 'cart/cart.html', context)

def order(request, id):
    order = OrdersModel.objects.get(id=id)
    order.status = 1
    order.description = request.POST.get("description")

    order_detail = OrdersDetailModel.objects.filter(orders=order)
    for item in order_detail:
        item.price = item.product.price
        item.save()
    
    order.save()

    context = {
        "order": order
    }
    return render(request, 'cart/order.html', context)

def add_to_cart(request, id):
    add_to_cart_common(request, id)
    return redirect("cart:cart")

def add_to_cart_common(request, id):
    product = ProductModel.objects.get(id=id)
    customer = CustomerModel.objects.get(user=request.user)

    order, created = OrdersModel.objects.get_or_create(
        customer = customer,
        status = 0
    )

    try:
        order_detail = OrdersDetailModel.objects.get(
            orders = order,
            product = product
        )
    except OrdersDetailModel.DoesNotExist:
        order_detail = OrdersDetailModel(
            orders = order,
            product = product,
            quantity = 0,
            price = product.price,
        )
    
    order_detail.quantity = order_detail.quantity + 1 if order_detail.quantity else 1
    order_detail.price = product.price
    order_detail.save()
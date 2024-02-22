from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from customer.models import CustomerModel
from orders.models import OrdersModel
from orders_detail.models import OrdersDetailModel


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
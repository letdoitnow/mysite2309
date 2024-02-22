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


    context = {
        "customer": customer
    }
    return render(request, 'cart/cart.html', context)

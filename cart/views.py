from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from customer.models import CustomerModel


# Create your views here.
def cart(request):
    customer = CustomerModel.objects.get(user=request.user)
    context = {
        "customer": customer
    }
    return render(request, 'cart/cart.html', context)

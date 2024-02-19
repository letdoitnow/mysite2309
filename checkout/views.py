from django.shortcuts import render
from product.models import ProductModel
from customer.models import CustomerModel


# Create your views here.
def checkout(request, id):
    product = ProductModel.objects.get(id=id)
    customer = CustomerModel.objects.get(user=request.user)
    context = {
        "product": product,
        "customer": customer,
    }
    return render(request, 'checkout/checkout.html', context)

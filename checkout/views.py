from django.shortcuts import render

# Create your views here.
def checkout(request, id):
    context = {
        "id": id
    }
    return render(request, 'checkout/checkout.html', context)

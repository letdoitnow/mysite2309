from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def cart(request):
    context = {
        
    }
    return render(request, 'cart/cart.html', context)

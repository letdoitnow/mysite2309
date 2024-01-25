from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login2(request):
    next = request.GET.get("next")
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_auth = authenticate(username=username, password=password)
        if is_auth:
            login(request, is_auth)
            if next:
                return redirect(next)    
            return redirect("home:home")
        
        error = "Tai khoan hoac Mat khau khong dung"

    context = {
        "error": error
    }
    return render(request, 'login2/login2.html', context)

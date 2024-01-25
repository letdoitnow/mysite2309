from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def logout2(request):
    logout(request)
    return redirect("login2:login2")
from django.shortcuts import render, redirect

# Create your views here.
def logout2(request):
    return redirect("login2:login2")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is Home page")

def about(request):
    return HttpResponse("Day la trang Gioi thieu")
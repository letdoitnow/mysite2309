from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return HttpResponse("Blog page")

def blog_detail(request):
    return HttpResponse("Blog detail page")

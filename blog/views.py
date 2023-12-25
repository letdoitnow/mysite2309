from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    return render(request, 'blog/blog_list.html')

def blog_detail(request):
    return render(request, 'blog/blog_detail.html')

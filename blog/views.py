from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    context = {
        'posts': [
            {
                "title": "tieu de bai viet 1",
                "summary": "noi dung tom tat 1",
            },
            {
                "title": "tieu de bai viet 2",
                "summary": "noi dung tom tat 2",
            },
            {
                "title": "tieu de bai viet 3",
                "summary": "noi dung tom tat 3",
            },
        ]
    }
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request):
    context = {
        "title": "tieu de bai viet 1",
        "summary": "noi dung tom tat 1",
        "body": "noi dung chi tiet 1",
        "author": "tac gia",
    }
    return render(request, 'blog/blog_detail.html', context)

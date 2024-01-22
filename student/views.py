from django.shortcuts import render, redirect
from .models import StudentModel
from .forms import StudentForm
from django.db.models import Q
from django.conf import settings

# Create your views here.
def student_list(request):
    # search
    keyword = request.GET.get("keyword")
    if keyword:
        students = StudentModel.objects.filter(
            Q(last_name__contains=keyword)
            | Q(first_name__contains=keyword)
        )
    else:
        students = StudentModel.objects.all()

    # sort
    sort = request.GET.get("sort")
    if sort not in ["first_name", "-mark_math", "-mark_literature", "-mark_english", "-mark_total"]:
        sort = settings.DEFAULT_SORT

    if sort == "-mark_total":
        students = sorted(
            students, 
            key=lambda sv:sum([sv.mark_math, sv.mark_literature, sv.mark_english]), 
            reverse=True
        )
    else:
        students = students.order_by(sort)

    context = {
        "students": students,
        "keyword": keyword if keyword else "",
    }
    return render(request, 'student/student_list.html', context)

def student_detail(request, id):
    sv = StudentModel.objects.get(id=id)
    context = {
        "sv": sv
    }
    return render(request, 'student/student_detail.html', context)

def student_add(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student:student_list")

    context = {
        "form": form
    }
    return render(request, 'student/student_add.html', context)

def student_update(request, id):
    model = StudentModel.objects.get(pk=id)
    form = StudentForm(instance=model)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect("student:student_detail", id)

    context = {
        "form": form
    }
    return render(request, 'student/student_update.html', context)

def student_delete(request, id):
    model = StudentModel.objects.get(pk=id)
    model.delete()
    return redirect("student:student_list")

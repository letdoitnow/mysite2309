from django.shortcuts import render, redirect
from .models import StudentModel
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = StudentModel.objects.all().order_by("-created_at")

    context = {
        "students": students
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

from django.shortcuts import render
from .models import StudentModel

# Create your views here.
def student_list(request):
    students = StudentModel.objects.all().order_by("-created_at")

    context = {
        "students": students
    }
    return render(request, 'student/student_list.html', context)
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodosModel
from .serializers import TodosSerializer

# Create your views here.
@api_view(["GET", "POST"])
def todos_list_api(request):
    if request.method == "GET":
        model = TodosModel.objects.all()
        serializer = TodosSerializer(model, many=True)
        return Response(data=serializer.data)
    
    if request.method == "POST":
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def todos_detail_api(request, id):
    try:
        model = TodosModel.objects.get(id=id)
    except TodosModel.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = TodosSerializer(model)
        return Response(data=serializer.data)
    
    if request.method == "PUT":
        serializer = TodosSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        model.delete()
        return Response()

def todos_list(request):
    context = {

    }
    return render(request, 'todos/todos_list.html', context)
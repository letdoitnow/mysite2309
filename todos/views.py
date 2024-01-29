from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodosModel
from .serializers import TodosSerializer

# Create your views here.
@api_view(["GET", "POST"])
def todos_list(request):
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


@api_view(["GET"])
def todos_detail(request, id):
    model = TodosModel.objects.get(id=id)
    serializer = TodosSerializer(model)
    return Response(data=serializer.data)

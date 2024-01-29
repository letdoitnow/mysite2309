from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodosModel
from .serializers import TodosSerializer

# Create your views here.
@api_view(["GET"])
def todos_list(request):
    model = TodosModel.objects.all()
    serializer = TodosSerializer(model, many=True)
    return Response(data=serializer.data)

@api_view(["GET"])
def todos_detail(request, id):
    model = TodosModel.objects.get(id=id)
    serializer = TodosSerializer(model)
    return Response(data=serializer.data)

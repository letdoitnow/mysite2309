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

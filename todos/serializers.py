from rest_framework import serializers
from .models import TodosModel

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodosModel
        fields = ["id", "title", "summary", "description", "status"]

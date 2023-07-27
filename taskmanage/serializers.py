from rest_framework import serializers
from .models import Tasksm

class TasksmSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tasksm
        fields = '__all__'
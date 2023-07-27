from rest_framework import viewsets
from . import models
from . import serializers

class TasksmViewset(viewsets.ModelViewSet):
    queryset = models.Tasksm.objects.all()
    serializer_class = serializers.TasksmSerializer
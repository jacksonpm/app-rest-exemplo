# ViewSets define the view behavior.
from rest_framework import viewsets

from app1.model.task import Task
from app1.serializer.task_serializer import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

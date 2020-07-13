# Serializers define the API representation.
from rest_framework import serializers

from app1.model.task import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'job', 'created_at', 'deleted_at']



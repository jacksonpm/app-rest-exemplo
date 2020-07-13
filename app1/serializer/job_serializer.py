# Serializers define the API representation.
from rest_framework import serializers

from app1.model.job import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ['code', 'name', 'address', 'formated_state', 'number', 'tasks']

# ViewSets define the view behavior.
from rest_framework import viewsets

from app1.model.job import Job
from app1.serializer.job_serializer import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

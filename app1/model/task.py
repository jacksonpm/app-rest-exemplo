from django.db.models import *

from app1.model.base_model import BaseModel
from app1.model.job import Job


class Task(BaseModel):
    name = CharField(max_length=255, verbose_name="Task Name", default="")
    job = ForeignKey(Job, on_delete=CASCADE, verbose_name="Job", related_name='tasks')

    def __str__(self):
        return str(self.pk).zfill(6) + ' - ' + str(self.name)

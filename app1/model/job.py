from django.db.models import *

from app1.model.base_model import BaseModel

STATES = (
    (1, 'AM'),
    (2, 'ES'),
    (3, 'MG'),
    (4, 'BH'),
    (5, 'RO'),
)


class Job(BaseModel):
    name = CharField(max_length=255, verbose_name="Job Name", default="")
    address = CharField(max_length=255, verbose_name="Address", default="")
    state = IntegerField(choices=STATES)
    number = CharField(default='', max_length=255)

    def formated_state(self):
        return self.get_state_display()

    def code(self):
        return str(self.pk).zfill(6)

from django.db.models import *


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True, editable=False)
    deleted_at = DateTimeField(default=None, null=True, blank=True, editable=False)

    class Meta:
        abstract = True

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class BaseModel(models.Model):
    id: "models.UUIDField[uuid.UUID, uuid.UUID]" = models.UUIDField(
        verbose_name=_("ID"), primary_key=True, default=uuid.uuid4, editable=False
    )

    class Meta(TypedModelMeta):
        abstract = True

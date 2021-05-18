from django.db import models
import uuid


class Intent(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    intent = models.CharField(max_length=128)

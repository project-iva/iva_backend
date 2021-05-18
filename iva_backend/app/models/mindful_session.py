from django.db import models
import uuid


class MindfulSession(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    source_name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()

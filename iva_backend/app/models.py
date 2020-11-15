from django.db import models
import uuid


class Intent(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    intent = models.CharField(max_length=128)


class TrainingInstance(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_text = models.TextField()
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, related_name='training_instances')
    created_at = models.DateTimeField(auto_now_add=True)

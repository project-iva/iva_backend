from django.db import models
import uuid


class MindfulSession(models.Model):
    uuid = models.UUIDField(primary_key=True)
    source_name = models.CharField(max_length=128)
    start = models.DateTimeField()
    end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def duration_in_secs(self) -> float:
        return (self.end - self.start).total_seconds()

    class Meta:
        ordering = ('-created_at',)

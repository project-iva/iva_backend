import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iva_backend.settings")
app = Celery("iva_backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(['iva_backend.app'])

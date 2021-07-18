import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iva_backend.settings")
app = Celery("iva_backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(['iva_backend.app'])
app.conf.beat_schedule = {
    # Executes every hour
    'store-asset-prices': {
        'task': 'iva_backend.app.tasks.store_asset_prices',
        'schedule': crontab(minute=0),
    },
}

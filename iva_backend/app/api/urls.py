from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers

from iva_backend.app.api.views.intents import IntentsViewSet
from iva_backend.app.api.views.training_instances import TrainingInstancesViewSet, TrainingInstancesExportView

router = routers.SimpleRouter()
router.register(r'intents', IntentsViewSet)
router.register(r'training-instances', TrainingInstancesViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('export-training-instances/', TrainingInstancesExportView.as_view()),
]

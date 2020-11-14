from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers

from iva_backend.app.api.views.intent import IntentViewSet
from iva_backend.app.api.views.training_instances import TrainingInstanceViewSet

router = routers.SimpleRouter()
router.register(r'intents', IntentViewSet)
router.register(r'training-instances', TrainingInstanceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

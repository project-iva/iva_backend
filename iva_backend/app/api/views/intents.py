from rest_framework import viewsets

from iva_backend.app.api.serializers.intent_seliazer import IntentSerializer
from iva_backend.app.models.intent import Intent


class IntentsViewSet(viewsets.ModelViewSet):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

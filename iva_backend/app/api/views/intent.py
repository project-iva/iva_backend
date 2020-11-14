from rest_framework import viewsets, mixins

from iva_backend.app.api.serializers import IntentSerializer
from iva_backend.app.models import Intent


class IntentViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

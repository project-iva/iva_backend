from rest_framework import viewsets
from iva_backend.app.api.serializers import TrainingInstanceSerializer
from iva_backend.app.models import TrainingInstance


class TrainingInstanceViewSet(viewsets.ModelViewSet):
    queryset = TrainingInstance.objects.all()
    serializer_class = TrainingInstanceSerializer

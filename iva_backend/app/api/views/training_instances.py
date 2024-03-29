from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.training_instance import TrainingInstanceSerializer, \
    ExportTrainingInstancesSerializer
from iva_backend.app.models.training_instance import TrainingInstance


class TrainingInstancesViewSet(viewsets.ModelViewSet):
    queryset = TrainingInstance.objects.all()
    serializer_class = TrainingInstanceSerializer


class TrainingInstancesExportView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        queryset = TrainingInstance.objects.filter(approved=True)
        serializer = ExportTrainingInstancesSerializer(queryset, many=True)
        response = Response(serializer.data)
        response['Content-Disposition'] = 'attachment'
        return response

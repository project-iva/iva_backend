from itertools import groupby

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.assets import AssetTrackerEntriesGroupedByDateSerializer
from iva_backend.app.models import AssetTrackerEntry


class AssetsView(APIView):
    def get(self, request) -> Response:
        queryset = AssetTrackerEntry.objects.order_by('-date')
        result = [{'date': key, 'asset_tracker_entries': list(group)} for key, group in
                  groupby(queryset,
                          key=lambda asset_tracker_entry: timezone.localtime(asset_tracker_entry.date))]

        serializer = AssetTrackerEntriesGroupedByDateSerializer(data=result, many=True)
        serializer.is_valid()
        return Response(serializer.data)

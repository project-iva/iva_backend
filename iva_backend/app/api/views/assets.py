from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.assets import AssetTrackerEntriesGroupedByDateSerializer
from iva_backend.app.models import AssetTrackerEntry


class AssetsView(APIView):
    def get(self, request):
        dates = AssetTrackerEntry.objects.values_list('date', flat=True).order_by().distinct()
        data = []
        print('aa')
        for date in dates:
            entries = AssetTrackerEntry.objects.filter(date=date)
            data.append({
                'date': date,
                'asset_tracker_entries': entries
            })
        serializer = AssetTrackerEntriesGroupedByDateSerializer(data=data, many=True)
        serializer.is_valid()
        return Response(serializer.data)

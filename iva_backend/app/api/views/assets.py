from datetime import timedelta, datetime, time
from itertools import groupby
from django.utils.timezone import make_aware

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from iva_backend.app.api.serializers.assets import AssetTrackerEntriesGroupedByDateSerializer, \
    AssetDayPriceChangeSerializer
from iva_backend.app.models import AssetTrackerEntry, Asset


class AssetTrackerEntriesView(APIView):
    def get(self, request) -> Response:
        queryset = AssetTrackerEntry.objects.order_by('-date')
        result = [{'date': key, 'asset_tracker_entries': list(group)} for key, group in
                  groupby(queryset,
                          key=lambda asset_tracker_entry: timezone.localtime(asset_tracker_entry.date))]

        serializer = AssetTrackerEntriesGroupedByDateSerializer(data=result, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class AssetsDayPriceChangeView(APIView):
    def get(self, request) -> Response:
        results = []
        for asset in Asset.objects.all():
            tracker_entries_qs = asset.tracker_entries
            last_entry = tracker_entries_qs.last()
            last_entry_date = last_entry.date.date()
            prev_day_date = last_entry_date - timedelta(1)

            prev_day_start = make_aware(datetime.combine(prev_day_date, time()))
            prev_day_end = make_aware(datetime.combine(last_entry_date, time()))
            prev_day_entries_qs = tracker_entries_qs.filter(date__gte=prev_day_start, date__lt=prev_day_end)
            prev_day_last_entry = prev_day_entries_qs.last()
            results.append({
                'asset': asset,
                'last_entry': last_entry,
                'prev_day_last_entry': prev_day_last_entry
            })

        serializer = AssetDayPriceChangeSerializer(data=results, many=True)
        serializer.is_valid()
        return Response(serializer.data)

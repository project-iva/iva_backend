from rest_framework import serializers

from iva_backend.app.models import AssetTrackerEntry, Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        exclude = ['id']


class AssetTrackerEntrySerializer(serializers.ModelSerializer):
    asset = AssetSerializer(read_only=True)

    class Meta:
        model = AssetTrackerEntry
        fields = ['value', 'market_price', 'asset']


class AssetTrackerEntriesGroupedByDateSerializer(serializers.Serializer):
    asset_tracker_entries = AssetTrackerEntrySerializer(many=True)
    date = serializers.DateTimeField()

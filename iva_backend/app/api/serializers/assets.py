from rest_framework import serializers

from iva_backend.app.models import AssetTrackerEntry, Asset


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        exclude = ['id']


class AssetTrackerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetTrackerEntry
        fields = ['value', 'market_price']


class AssetTrackerEntryWithAssetSerializer(AssetTrackerEntrySerializer):
    asset = AssetSerializer(read_only=True)

    class Meta(AssetTrackerEntrySerializer.Meta):
        fields = AssetTrackerEntrySerializer.Meta.fields + ['asset']


class AssetTrackerEntriesGroupedByDateSerializer(serializers.Serializer):
    asset_tracker_entries = AssetTrackerEntryWithAssetSerializer(many=True)
    date = serializers.DateTimeField()


class AssetDayPriceChangeSerializer(serializers.Serializer):
    asset = AssetSerializer()
    last_entry = AssetTrackerEntrySerializer()
    prev_day_last_entry = AssetTrackerEntrySerializer()

from datetime import datetime

from django.conf import settings
from django.db import IntegrityError
from django.utils import timezone

from iva_backend.app.iexcloud_api import IEXCloudAPI, IEXCloudAPIError
from iva_backend.app.models import Asset, AssetTrackerEntry
from iva_backend.celery import app


def create_asset_tracker_entry(asset: Asset, price: float, date: datetime):
    try:
        asset_volume = asset.current_volume
        AssetTrackerEntry.objects.create(asset=asset, value=price*asset_volume, market_price=price, date=date)
    except IntegrityError:
        pass


@app.task
def store_asset_prices():
    iex_api = IEXCloudAPI(settings.IEX_CLOUD_API_TOKEN)
    # using the same datetime makes the grouping easier
    date = timezone.now()
    for asset in Asset.objects.all():
        try:
            if asset.type == Asset.Type.STOCK:
                price = iex_api.get_stock_price(asset.ticker)
            elif asset.type == Asset.Type.CRYPTO:
                price = iex_api.get_crypto_price(asset.ticker)
            else:
                # skip over different type of assets
                continue
        except IEXCloudAPIError:
            continue
        else:
            create_asset_tracker_entry(asset, price, date)

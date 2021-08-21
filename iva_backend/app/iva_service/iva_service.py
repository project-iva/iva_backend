import requests
from django.conf import settings
from requests.exceptions import ConnectionError


class IvaService:
    @staticmethod
    def send_day_plan_changed_notification():
        url = settings.IVA_URL + '/day-plan-changed/'
        try:
            requests.post(url)
        except ConnectionError:
            pass

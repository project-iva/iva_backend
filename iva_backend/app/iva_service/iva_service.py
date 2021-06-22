import requests
from django.conf import settings
from requests.exceptions import ConnectionError


class IvaService:
    @staticmethod
    def send_mindful_session_created_notification():
        url = settings.IVA_URL + '/mindful_session_recorded'
        try:
            requests.post(url)
        except ConnectionError:
            pass

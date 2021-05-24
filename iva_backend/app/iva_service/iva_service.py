import requests
from django.conf import settings


class IvaService:
    @staticmethod
    def send_mindful_session_created_notification():
        url = settings.IVA_URL + '/mindful_session_recorded'
        requests.post(url)

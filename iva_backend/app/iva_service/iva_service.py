from enum import Enum

import requests
from django.conf import settings
from requests.exceptions import ConnectionError


class IvaService:
    class DataUpdatedType(str, Enum):
        CALORIES = 'CALORIES',
        BODY_MASS = 'BODY_MASS',
        DAY_PLAN = 'DAY_PLAN',
        DAY_GOALS = 'DAY_GOALS',
        SLEEP = 'SLEEP',
        MINDFUL_SESSIONS = 'MINDFUL_SESSIONS'

    @staticmethod
    def send_data_updated_notification(data_type: DataUpdatedType):
        try:
            url = settings.IVA_URL + '/backend-data-updated/'
            requests.post(url, data={'data_type': data_type})
        except ConnectionError:
            pass

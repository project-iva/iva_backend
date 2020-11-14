from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'iva_backend.app'

    def ready(self):
        import iva_backend.app.signals

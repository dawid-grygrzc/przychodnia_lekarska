from django.apps import AppConfig


class RejConfig(AppConfig):
    name = 'rej'

    def ready(self):
        import rej.signals

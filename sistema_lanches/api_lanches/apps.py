from django.apps import AppConfig

class ApiLanchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_lanches'

    def ready(self):
        import api_lanches.signals


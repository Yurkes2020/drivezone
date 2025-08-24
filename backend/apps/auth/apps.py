from django.apps import AppConfig


class RegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.auth'
    label = 'auth_'
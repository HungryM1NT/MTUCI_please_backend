from django.apps import AppConfig


class FirstLevelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'first_level'

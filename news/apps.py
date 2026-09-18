from django.apps import AppConfig
import os


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    def ready(self):
        # جلوگیری از اجرای دوباره به‌خاطر auto-reloader جنگو در حالت DEBUG
        if os.environ.get('RUN_MAIN') != 'true':
            return
        from .scheduler import start
        start()





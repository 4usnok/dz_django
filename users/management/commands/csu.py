from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Настройки для переопределенного супер-юзера"""
        user = User.objects.create(email="chusnok25@yandex.ru")
        user.set_password("6qndea3c8")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

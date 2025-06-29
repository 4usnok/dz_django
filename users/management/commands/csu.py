from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Настройки для переопределенного супер-юзера"""
        user = User.objects.create(email="admin@example.com")
        user.set_password("10121331")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

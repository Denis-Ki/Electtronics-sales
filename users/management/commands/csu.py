from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin_1@example.com", username="Админ Админов")
        user.set_password("admin")
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True).exists():
            print('すでにスーパーユーザーがいるので、作成をスキップ')
        else:
            User.objects.create_superuser(
                username='admin', email='admin@admin.com', password='admin123',
                is_superuser=True, is_staff=True, is_active=True
            )

# server/myproject/api/management/commands/clear_users.py
from django.core.management.base import BaseCommand
from api.models import User

class Command(BaseCommand):
    help = 'Deletes all users from the database'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users'))
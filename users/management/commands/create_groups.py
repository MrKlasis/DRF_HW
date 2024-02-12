from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create initial groups'

    def handle(self, *args, **options):
        Group.objects.get_or_create(name='moderator')
        Group.objects.get_or_create(name='other_group')

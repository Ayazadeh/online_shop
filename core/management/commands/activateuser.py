from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError
from customer.models import *


class Command(BaseCommand):
    help = 'active and de active user'

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument('username',
                            metavar='user_name',
                            help="name of user")

    def handle(self, *args, **options):
        username1 = options['username']
        try:
            customer = User.objects.get(username=username1)
            customer.is_active = True
            customer.save()
        except Exception as e:
            print(e)


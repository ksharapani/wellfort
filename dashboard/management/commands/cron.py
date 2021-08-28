from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--site', dest='site', required=True, help='the site to process')

    def handle(self, *args, **options):
        try:
            print('Starting Learning.....')

            site = options['name']

            if site == 'twitter_sentiment':
                pass

        except Exception as e:
            raise CommandError(repr(e))

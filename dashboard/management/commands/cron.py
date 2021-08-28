from gtts import gTTS
from django.core.management.base import BaseCommand, CommandError

from dashboard.models import Message


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--name', dest='name', required=True, help='name of the cron')

    def handle(self, *args, **options):
        try:
            print('Starting Learning.....')

            site = options['name']

            if site == 'audio':
                language = 'en'
                messages = Message.objects.all()

                for message in messages:
                    audio = gTTS(text=message.message, lang=language, slow=False)

                    audio.save("static/audio/{}.mp3".format(message.message_id))

        except Exception as e:
            raise CommandError(repr(e))

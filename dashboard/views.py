from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count, F
from django.utils.timezone import datetime

from dashboard.models import Queue


class Dashboard(APIView):

    def get(self, request):
        today = datetime.today()
        data = Queue.objects.filter(displayed=False).order_by('created_at').first()

        queue_data = Queue.objects.filter(created_at__year=today.year, created_at__month=today.month,
                                          created_at__day=today.day).values(user=F('clicked_user__name')).\
            annotate(count=Count('clicked_user')).order_by()

        output = {'status': 'failed', 'user': None, 'display_message': None, 'audio': None, 'data': queue_data}
        if data:
            output = {'user': data.clicked_user.name, 'status': 'successful',
                      'display_message': data.display_message.message, 'audio': data.display_message.audio.url,
                      'data': queue_data}
            data.displayed = True
            data.save()

        return Response(output)

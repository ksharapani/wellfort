from rest_framework.response import Response
from rest_framework.views import APIView

from dashboard.models import Queue


class Dashboard(APIView):

    def get(self, request):
        queue_data = Queue.objects.all().filter(displayed=False).order_by('created_at')

        output = {'status': 'failed'}
        for queue_id, data in enumerate(queue_data):
            if queue_id == 0:
                output = {'user': data.clicked_user.name, 'status': 'successful',
                          'display_message': data.display_message.message}
                data.displayed = True
                data.save()

            print(data)

        return Response(output)

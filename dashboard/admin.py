from django.contrib import admin
from dashboard.models import Queue, User, Message


admin.site.register(Queue)
admin.site.register(User)
admin.site.register(Message)

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=512)
    pin_number = models.IntegerField()


class Message(models.Model):
    message_id = models.IntegerField()
    message = models.CharField(max_length=512)
    audio = models.FileField(upload_to='static/audio/', blank=True)


class Queue(models.Model):
    objects = None

    clicked_user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_message = models.ForeignKey(Message, on_delete=models.CASCADE)
    displayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)

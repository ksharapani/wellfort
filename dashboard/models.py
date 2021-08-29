from django.db import models


class User(models.Model):
    objects = None

    name = models.CharField(max_length=512)
    pin_number = models.IntegerField()

    def __str__(self):
        return self.name


class Message(models.Model):
    objects = None

    message_id = models.IntegerField()
    message = models.CharField(max_length=512)

    def __str__(self):
        return self.message


class Queue(models.Model):
    objects = None

    clicked_user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_message = models.ForeignKey(Message, on_delete=models.CASCADE)
    displayed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.created_at)

'''Models'''
from django.db import models
from E_learning_app.models import CustomUser

class GroupName(models.Model):
    '''Manage groups'''
    name = models.CharField(max_length=250)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Message(models.Model):
    '''Manage messages'''
    message = models.TextField()
    messagetime = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    group = models.ForeignKey(GroupName, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.messagetime)

'''Register models'''
from django.contrib import admin
from .models import GroupName, Message

@admin.register(Message)
class MessageModel(admin.ModelAdmin):
    '''Display model fields'''
    list_display = ['id', 'message', 'messagetime', 'group']

@admin.register(GroupName)
class GroupNameModel(admin.ModelAdmin):
    '''Display model fields'''
    list_display = ['id', 'user', 'name']

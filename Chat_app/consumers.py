'''Websocket Handling'''
import json
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
from channels.db import database_sync_to_async
from .models import Message, GroupName
import cv2
import base64
import time
import asyncio


class MyAsyncConsumer(AsyncConsumer):
    '''Websocket Connection'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = None

    async def websocket_connect(self, event):
        '''Connecting...'''
        await self.send({
            'type': 'websocket.accept'
        })
        self.group_name = self.scope['url_route']['kwargs']['channel_name']
        await self.channel_layer.group_add(self.group_name, self.channel_name)

    async def websocket_receive(self, event):
        '''Message Receiving...'''
        group_name = await database_sync_to_async(GroupName.objects.filter(name=self.group_name)\
        .first)()
        user_message = event['text']
        messages = Message(message=user_message, group=group_name, username=\
        self.scope['user'].get_full_name())
        data_message = {'userName': self.scope['user'].get_full_name(), 'message': user_message}
        await database_sync_to_async(messages.save)()
        await self.channel_layer.group_send(self.group_name, {'type': 'chat.message',\
        'message': json.dumps(data_message)})

    async def websocket_disconnect(self, event):
        '''Disconnecting...'''
        # await self.send({'type': 'websocket.send', 'text': self.scope['user'].username})
        await self.channel_layer.group_send(self.group_name, {'type': 'chat.message',\
        'message': self.scope['user'].get_full_name()})
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()

    async def chat_message(self, event):
        '''Handling group messages'''
        if 'userName' in event['message']:
            message_data = json.loads(event['message'])
            data_message = {'message': message_data['message'],\
            'userName': message_data['userName']}
            await self.send({'type': 'websocket.send', 'text': json.dumps(data_message)})
        else:
            await self.send({'type': 'websocket.send', 'text': event['message']})
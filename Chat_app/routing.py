'''Manage route paths'''
from django.urls import path
from .consumers import MyAsyncConsumer


websocket_urls = [
    path('channel-name/<str:channel_name>/', MyAsyncConsumer.as_asgi()),
]

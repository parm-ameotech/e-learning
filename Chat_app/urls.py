'''Managing URLS'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('channel-name/<str:channel_name>', views.channel_page, name = 'channel-name'),
    path('clear-delete', views.clear_delete, name='clear-delete'),

]
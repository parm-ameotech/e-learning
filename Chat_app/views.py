'''Liberary'''
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import GroupName, Message

def index(request):
    '''Home Page'''
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'chat_index.html')

def channel_page(request, channel_name):
    '''Channel Page'''
    if not request.user.is_authenticated:
        return redirect('login')
    exists_group = GroupName.objects.filter(name=channel_name).first()
    messages = []
    if not exists_group:
        group = GroupName(user=request.user, name=channel_name)
        group.save()
        channel_name = group.name
    else:
        messages = Message.objects.filter(group=exists_group)
        channel_name = exists_group.name
    return render(request, 'channel.html', {'channel_name': channel_name, 'messages': messages})


def clear_delete(request):
    '''Delete group and clear chat'''
    response = {}
    response['status'] = False
    if request.user.is_authenticated:
        if request.method == 'POST':
            status = request.POST.get('status', None)
            group_name = request.POST.get('group_name', None)
            if status == 'clear':
                Message.objects.all().delete()
                response['status'] = True
            else:
                GroupName.objects.filter(name=group_name).first().delete()
                response['status'] = True
    return JsonResponse(response)
from django.shortcuts import render
# from django.http import HttpResponse
from . models import Room 


# what is the user sending to the backend 

list_items = [
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'Design with me' },
    {'id':3, 'name':'frontend developer'}
]


def home(request):
    rooms = Room.objects.all()
    context = {'list_items':rooms}
    return render(request, "base/home.html", context)

def rooms(request, pk):
    # we are just setting the specific pk to the room 
    #  if not its a None
    # room = None 
    # for i in list_items:
    #     if i['id'] == int(pk):
    #         room = i 
    room = Room.objects.get(id=pk)
    context = {"room":room}
    return render(request, "base/gain.html", context)

def createRoom(request): 
    context = {}
    return render(request, 'base/room_form.html', context)
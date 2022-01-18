from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id':1, 'name': 'learn pyhton'},
#     {'id':2, 'name': 'learn java'},
#     {'id':3, 'name': 'learn javascript'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}            
    return render(request, 'base/room.html', context)

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import string

# Create your views here.
def index(request):
  if request.method == 'POST':
    roomname = 'RandomRoom' if request.POST.get('roomname') == "" else request.POST.get('roomname')
    username = 'Anonymous' if request.POST.get('username') == "" else request.POST.get('username')
    user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return HttpResponseRedirect(reverse('rooms',args=[roomname,username,user_id]))
  return render(request, 'chatroom/index.html')

def rooms(request,roomname, user, user_id):
  return render(request, 'chatroom/rooms.html', {
    'roomname': roomname,
    'user': user,
    'user_id': user_id
  })

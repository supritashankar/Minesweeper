from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def newgame(request):
  return render_to_response('frontend/newgame.html')

def display_mine(request, level):
  values = {0:1,1:1,2:0,3:1}
  level = 'Beginner'
  return render_to_response('frontend/beg-game.html', locals())

import requests

from django.shortcuts import render, render_to_response

def newgame(request):
  return render_to_response('frontend/newgame.html')

def display_mine(request, level):
  values = {0:1,1:1,2:0,3:1}
  level = 'Beginner'
  return render_to_response('frontend/beg-game.html', locals())

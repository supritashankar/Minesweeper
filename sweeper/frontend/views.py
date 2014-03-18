from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def newgame(request):
  return render_to_response('frontend/newgame.html')

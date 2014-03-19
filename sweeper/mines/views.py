import json
import random

from django.shortcuts import render
from django.http import HttpResponse

def randomize(request, n):
  grid = []
  for i in range(0,int(n)):
    grid.append(int(random.getrandbits(1)))
    message = {'grid' : grid}
  return HttpResponse(json.dumps(message), mimetype = 'application/json')   

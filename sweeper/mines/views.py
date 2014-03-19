import json

from django.shortcuts import render
from django.http import HttpResponse

def randomize(request, n):
  grid = ''
  for i in range(1,n)
    grid.append(int(random.getrandbits(1)))
  message = {'grid' : grid}
  return HttpResponse(json.dumps(message), mimetype = 'application/json')   

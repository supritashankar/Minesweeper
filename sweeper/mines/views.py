import json

from django.shortcuts import render
from django.http import HttpResponse

def randomize(request, n):
  grid = ''
  if n == '3':
    grid = '100'

  if n == '6':
    grid = '100101'

  message = {'grid' : grid}
  return HttpResponse(json.dumps(message), mimetype = 'application/json')   

import json
import random
from random import shuffle

from django.shortcuts import render
from django.http import HttpResponse

def randomize(request, num_cells, num_mines):
  grid = [1]*int(num_cells)
  mines = [[i] for i in range(0,int(num_cells))]
  shuffle(mines)
  mines = mines[:int(num_mines)]
  for i in mines:
    grid[i[0]] = 0
  message = {'grid' : grid}
  return HttpResponse(json.dumps(message), mimetype = 'application/json')   

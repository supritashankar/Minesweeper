import json
import random

from django.shortcuts import render
from django.http import HttpResponse

def randomize(request, num_cells, num_mines):
  grid = [1]*num_cells
  mines = [[i] for i in range(num_cells)]
  shuffle(mines)
  mines = mines[:10]
  for i in mines:
    grid[i] = 0
  message = {'grid' : grid}
  return HttpResponse(json.dumps(message), mimetype = 'application/json')   

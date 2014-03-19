import requests

from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

def newgame(request):
  return render_to_response('frontend/newgame.html')

def display_mine(request, level):
  c = {}
  if level == 'B':
    values = {0:1,1:1,2:1,3:0, 4:1, 5:1, 6:1, 7:1, 8:1}
    response = requests.get('http://127.0.0.1:8000/mines/randomize/3/')
    print response.content
    request.session['values'] = values
    c = { 'level' : 'Beginner', 'loopcounter': '3', 'values': values}
    c.update(csrf(request))

  if level == 'I':
    values = {0:1,1:1,2:0,3:1, 4:0, 5:1, 6:1, 7:1, 8:1, 9:0, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1}
    loopcounter = 4
    level = 'Intermediate'

  if level == 'E':
    values = {0:1,1:1,2:0,3:1, 4:0, 5:1, 6:1, 7:1, 8:1, 9:0, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:0, 17:0, 18:0, 19:0, 20:1, 21:1, 22:1, 22:1, 23:1, 24:1}
    loopcounter = 5
    level = 'Expert'
    
  return render_to_response('frontend/beg-game.html', c)

def game(request):
  print request.POST
  index = 3
  values = request.session['values']
  print values
  for key,value in values.iteritems():
    print key, index
    if index == int(key):
      if value == 0:
        return render_to_response('frontend/game-over.html')

      count = get_neighbour_count(index, values)
      values[key] = count
      break
  return render_to_response('frontend/game.html', locals())

def get_neighbour_count(index, values):

  neighbours = get_neighbours(index, values)
  count = 0
  for neighbour in neighbours:
    if neighbour == 1:
      count  = count + 1
  if count == 0:
    values[index] = -1
  return count

def get_neighbours(index, values):
  k = 0
  for i in range(0,3):
    for j in range(0,3):
      grid[i][j] = values[k]
      if k == index:
        p = i
        q = j
      k = k+1 
  neighbour = []
  neighbour.append(getRows(p-1), grid)
  neighbour.append(grid[p][q-1])
  neighbour.append(getRows(p+1), grid)
  neighbour.append(grid[p][q+1])
  return neighbour

def getRows(i, grid):
  rowe = []
  for j in range(0,3):
    rowe.append(grid[i][j])
  return rowe

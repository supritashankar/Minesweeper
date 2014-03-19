import requests

from django.shortcuts import render, render_to_response

def newgame(request):
  return render_to_response('frontend/newgame.html')

def display_mine(request, level):
  values = {0:1,1:1,2:0,3:1, 4:0, 5:1, 6:1, 7:1, 8:1}
  response = requests.get('http://127.0.0.1:8000/mines/randomize/3/')
  print response.content
  request.session['values'] = values
  level = 'Beginner'
  loopcounter = 3
  return render_to_response('frontend/beg-game.html', locals())

def game(request, level, index):
  values = request.session['values']
  values = {0:1,1:1,2:-1,3:1}
  for key,value in values.iteritems():
    if index == key:
      if value == -1:
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
  neigh = []
  neigh.append(getRows(p-1), grid)
  neigh.append(grid[p][q-1])
  neigh.append(getRows(p+1), grid)
  neigh.append(grid[p][q+1])
  return neigh

def getRows(i, grid):
  rowe = []
  for j in range(0,3):
    rowe.append(grid[i][j])
  return rowe

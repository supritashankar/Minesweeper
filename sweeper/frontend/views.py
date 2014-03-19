import requests

from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf

def newgame(request):
  return render_to_response('frontend/newgame.html')

def display_mine(request, level):
  c = {}
  
  """ When the beginner level is chosen """
  if level == 'B':
    values = {0:1,1:1,2:1,3:0, 4:1, 5:1, 6:1, 7:1, 8:1}
    response = requests.get('http://127.0.0.1:8000/mines/randomize/3/')
    print response.content
    request.session['values'] = values
    request.session['level'] = level
    level = 'Beginner' 
    loopcounter = 3
    values = values
    c.update(csrf(request))

  """ When the intermediate level is chosen """
  if level == 'I':
    values = {0:1,1:1,2:0,3:1, 4:0, 5:1, 6:1, 7:1, 8:1, 9:0, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1}
    loopcounter = 4
    level = 'Intermediate'

  """ When the expertise level is chosen """
  if level == 'E':
    values = {0:1,1:1,2:0,3:1, 4:0, 5:1, 6:1, 7:1, 8:1, 9:0, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:0, 17:0, 18:0, 19:0, 20:1, 21:1, 22:1, 22:1, 23:1, 24:1}
    loopcounter = 5
    level = 'Expert'
  
  """ Update the CSRF as you are doing a form post """

  c = { 'level' : level, 'loopcounter': loopcounter, 'values': values}
  c.update(csrf(request)) 
  return render_to_response('frontend/beg-game1.html', c)

""""
def game_recursion(request):
  values = request.session['values']
  count = 0
  # make the grid_value - which will have the values the counts
  # make the grid_state - which will decide whether it has to be open/closed
  # make the grid - which has the position of the mines
  #grid_state = [[-1,1,1],[1,1,-1],[1,1,-1]]
  #grid_value = [[4,0,1][1,1,2],[2,1,3]]
  #grid = [[1,0,1],[1,1,1],[1,1,0]]
  #state_stack = [] holds the ordering.
  grid_state, grid_value = get_neighbours(row, col, grid_state, grid_value, grid)
  return render_to_response('frontend/game.html', locals())

def get_neighbours(row, col, grid_state, grid_value, grid):
  for i in range(row-1, row+1):
    for j in range(col-1, col+1):
      if i or j < 0 or (i or j > n) or (i==row && j==col):
        continue
      if grid[i][j] == 1 and not marked:	#if not a mine
         # Also mark grid[row][col] as marked 
         state_stack.append([row,col])
         grid_state[row][col] = -1
         get_neighbours(i, j, grid_state, grid_value, grid)
      else:
        grid_value[row][col] = grid_value[row][col] + 1
  #pop the row and column from the state_stack and use the previous one to navigate
  return get_neighbours(row, col, grid_state, grid_value, grid)
"""

def game(request):
  """ Once the user opens a square """

  index = 5
  values = request.session['values']
  
  """ If the point happened to be a mine, end the game """
  for key,value in values.iteritems():
    if index == int(key):
      if value == 0:
        return render_to_response('frontend/game-over.html')

      
      count = get_neighbour_count(index, values)
      if count == 0:
        values[key] = -1
        index = index + 1
        game(request, index)
      values[key] = 8 - count #As we want the number of mines around
      break
  return render_to_response('frontend/game.html', locals())

def get_neighbour_count(index, values):
  """ Returns the neighbours who are mines """
  neighbours = get_neighbours(index, values)
  count = 0
  for neighbour in neighbours:
    if neighbour == 1:
      count  = count + 1

  """ If all the elements around are not mines then open them up all """
  if count == 0:
    values[index] = -1
  return count

def get_neighbours(index, values):

  """ Returns the neighbours of a given element """
  k = 0
  grid = [[0 for x in xrange(3)] for x in xrange(3)] 
  for i in range(0,3):
    for j in range(0,3):
      grid[i][j] = values[k]
      if k == index:
        p = i
        q = j
      k = k+1 
  neighbour = []

  """ All the 8 neighbours for a given element """
  neighbour.append(getRows(p-1), grid)
  neighbour.append(grid[p][q-1])
  neighbour.append(getRows(p+1), grid)
  neighbour.append(grid[p][q+1])
  return neighbour

def getRows(i, grid):
  """ Given a row returns all the elements of that row """

  rowe = []
  for j in range(0,3):
    rowe.append(grid[i][j])
    if grid[i][j] == 1:
      grid[i][j] = -1
  return rowe, grid

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
    loopcounter = 4
    level = 'Intermediate'

  """ When the expertise level is chosen """
  if level == 'E':
    loopcounter = 5
    level = 'Expert'
  
  """ Update the CSRF as you are doing a form post """

  c = { 'level' : level, 'loopcounter': loopcounter, 'values': values}
  c.update(csrf(request)) 
  return render_to_response('frontend/beg-game.html', c)


def game_recursion(request):
  # make the grid_value - which will have the values the counts
  # make the grid_state - which will decide whether it has to be open/closed
  # make the grid - which has the position of the mines

  """ If clicked on a mine the game is over """
  if grid[row][col] == 0:
    return render_to_response('frontend/end-of-game.html')

  state_stack = [] #holds the ordering
  marked = [[0 for x in xrange(3)] for x in xrange(3)]
  grid_state, grid_value = get_neighbours(row, col, grid_state, grid_value, grid, marked, state_stack)
  return render_to_response('frontend/game.html', locals())

def get_neighbours(row, col, grid_state, grid_value, grid, marked, state_stack):

  for i in range(row-1, row+1):
    for j in range(col-1, col+1):

      """ if the co-ordinates are out of the box, for instance when row=col=0, then i=j= -1 , it should not execute """
      if i or j < 0 or (i or j > 2) or (i==row and j==col):
        continue


      if marked[i][j] == 0:
        if grid[i][j] == 1:        #if not a mine
          marked[row][col] = 1

          # Follow DFS; Append it into the stack
          state_stack.append([row,col])

          #Make the cell open
	  grid_state[row][col] = -1

          #Move onto the next neighbour
          get_neighbours(i, j, grid_state, grid_value, grid, marked, state_stack)

        else:
          grid_value[row][col] = grid_value[row][col] + 1

      else:
        continue

  print state_stack
  state_stack = state_stack[:-1]
  rc = state_stack[-1:]

  """ To come out of recursion; it must finishing all recursion"""
  if i == row+1 and j == col+1 and len(state_stack) == 0:
    return

  return get_neighbours(row, col, grid_state, grid_value, grid, marked, state_stack)

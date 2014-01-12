# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    open = [[0, init[0], init[1]]]

    while (len(open)>0):
      current = open.pop(0)
      if current[1]==goal[0] and current[2]==goal[1]:
        return current
      for d in delta:
        next_i = current[1]+d[0]
        next_j = current[2]+d[1]
        if next_i>=0 and next_j>=0 and next_i<len(grid) and next_j<len(grid[0]) and grid[next_i][next_j]==0:
          open.append([current[0]+1, next_i, next_j])
          grid[next_i][next_j] = 1
    return -1

print search()

def relationship_status(from_member, to_member, social_graph):
    dictionary_1 = social_graph[from_member]['following']
    dictionary_2 = social_graph[to_member]['following']
    if from_member in dictionary_2 and to_member in dictionary_1:
        return("friends")
    elif from_member in dictionary_2:
        return('followed by')
    elif to_member in dictionary_1:
        return('follower')
    else:
        return('no relationship')
    
def tic_tac_toe(board):
  grid = len(board)
  y = 0

  for row in range(0, grid):
    if board[row].count(board[row][0]) == grid:
      if board[row][0] == "":
        return "NO WINNER"
      else:
        return(board[row][0])

  for column in range(0, grid):
    for x in range(0, grid):
      if board[x][column] == board[x-1][column]:
        y += 1
      else:
        y = 0
      if y == grid:
        if board[x][column] == "":
            return "NO WINNER"
        else:
          return(board[x][column])

  for i in range(0, grid):
    if board[i][i] == board[i-1][i-1]:
      y += 1
    else:
      y = 0
    if y == grid:
      if board[i][i] == "":
        return "NO WINNER"
      else:
        return(board[i][i])

  if y != grid:
    y = 0

  for i in range(1, grid):
    if board[grid - i][i - 1] == board[grid - i - 1][i]:
      y += 1
    else:
      y = 0
    if y == (grid -1):
      if board[grid-i-1][i] == "":
        return "NO WINNER"
      else:
        return(board[grid-i-1][i])

  if y != grid:
    return "NO WINNER"

    
def eta(first_stop, second_stop, route_map):
    total_traveltime = 0
    stopover = first_stop

    while stopover != second_stop:
        for leg in route_map:
            if leg[0] == stopover:
                total_traveltime += route_map[leg]['travel_time_mins']
                stopover = leg[1]
                break
    
    return total_traveltime
def print_line():
  print('---------')


def search(ch, rows):
  return [elm for row in rows for elm in row if elm == ch]


def column(matrix, i):
  return [row[i] for row in matrix]


def check_line(player, line):
  return all([elem == player for elem in line])


def check_rows(player, rows):
  return check_line(player, rows[0]) or \
         check_line(player, rows[1]) or \
         check_line(player, rows[2])


def check_cols(player, metrix):
  return check_line(player, column(metrix, 0)) or \
         check_line(player, column(metrix, 1)) or \
         check_line(player, column(metrix, 2))


def check_draw(metrix):
  return search('_', metrix)


def check_diagonals(ch, metrix):
  daigonal1 = [r[i] for i, r in enumerate(metrix)]
  daigonal2 = [r[-i - 1] for i, r in enumerate(metrix)]
  return check_line(ch, daigonal1) or check_line(ch, daigonal2)


def no_winners(metrix):
  return not winner("X", metrix) and not winner("O", metrix)


def winner(player, metrix):
  return check_rows(player, metrix) or \
         check_cols(player, metrix) or \
         check_diagonals(player, metrix)


cells = "_________"
metrix = [cells[:3], cells[3:6], cells[6:9]]
finished = False


def print_board(metrix):
  global finished
  print_line()
  for row in metrix:
    print('|', end=' ')
    for i in range(len(row)):
      print(f'{row[i]}', end=' ')
    print('|\n' if row != metrix[-1] else '|')
  print_line()

  # if winner("X", metrix) and winner("O", metrix) or \
  #         cells.count("X") - cells.count("O") > 1 or cells.count("O") - cells.count("X") > 1:
  #   print("Impossible")
  # else:
  # if search("_", metrix) and no_winners(metrix):
  #   print("Game not finished")
  if winner("X", metrix):  # case X wins
    print("X wins")
    finished = True
  elif winner("O", metrix):  # case O wins
    print("O wins")
    finished = True
  elif not search("_", metrix):
    print("Draw")
    finished = True


print_board(metrix)
player = "X"

while search("_", metrix) and not finished:
  player_inputs = input("Enter the coordinates").split(' ')

  if [x for x in player_inputs if not x.isnumeric()]:
    print("You should enter numbers!")
  else:
    cords = [int(s) for s in player_inputs]
    [row, col] = cords

    if [x for x in cords if 0 > x or x > 3]:
      print("Coordinates should be from 1 to 3!")
    elif metrix[row - 1][col - 1] != "_":
      print("This cell is occupied! Choose another one!")
    else:
      metrix[row - 1] = list(metrix[row - 1])
      metrix[row - 1][col - 1] = player
      "".join(metrix[row - 1])
      print_board(metrix)
      player = "X" if player == "O" else "O"

"""
1- take inputs -> split to array 
2- check if either sides wins:
  a.full row
  b.full column
  c.full diagonal
3- check if draw -> board capacity is full and no win
4- check if impossible -> one player have 2 more play over the other
"""


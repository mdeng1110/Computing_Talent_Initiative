def validate_sudoku_board(board):
  # validate each row
  # validate each column
  # validate sub-box
  for row in board:
    if not validate_row(row):
      return False
  #for columnIndex in range(0,9):
  if not validate_column(board):
    return False
  if not validate_boxes(board):
    return False
  return True

def validate_row(row):
  seen_numbers = set()
  for number in row:
    if number != "." and number in seen_numbers:
      return False
    else:
      seen_numbers.add(number)
  return True
  
def validate_column(board):
  for col_index in range(9):
    column = []
    for row_index in range(9):
      column.append(board[row_index][col_index])
    if not validate_row(column):
      return False
  return True
    
def validate_boxes(board):
  for row_index in range(0, 7, 3):
    for col_index in range(0, 7, 3):
      box = [
        board[row_index + 0][col_index + 0],
        board[row_index + 0][col_index + 1],
        board[row_index + 0][col_index + 2],
        
        board[row_index + 1][col_index + 0],
        board[row_index + 1][col_index + 1],
        board[row_index + 1][col_index + 2],
        
        board[row_index + 2][col_index + 0],
        board[row_index + 2][col_index + 1],
        board[row_index + 2][col_index + 2]
        ]
      if not validate_row(box):
        return False
  return True
input1 = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(validate_row(["5","3",".",".","7",".",".",".","."]))
print(validate_column(input1))
print(validate_sudoku_board(input1))
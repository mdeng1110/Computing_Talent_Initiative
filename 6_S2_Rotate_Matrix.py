def rotate_matrix(matrix):
  for row in matrix:
    print(row)
  print("---before---")
  
  for row in range(len(matrix)):
    for col in range(row, len(matrix)):
      #swapping
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
      
  for row in matrix:
    print(row)
  print("---after---")
  
  for row in matrix:
    row.reverse()
    print(row)
    
rotate_matrix([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
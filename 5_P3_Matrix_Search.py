def matrix_search(matrix, target):
  m = 0
  n = len(matrix)
  while n != m:
    mid = int((m + n) / 2)
    if matrix[mid][-1] > target:
      n = mid
    elif matrix[mid][-1] < target:
      m = mid + 1
    else:
      n = mid
  
  if m >= len(matrix):
    idx = m - 1
  else:
   idx = m
   
  i = 0
  j = len(matrix[idx])
  while i < j:
    mid = int((i + j) / 2) 
    # print("mid: ", mid)
    if matrix[idx][mid] > target:
      j = mid
    elif matrix[idx][mid] < target:
      i = mid + 1
    elif matrix[idx][mid] == target:
      return 1
  return 0
  
  # binary search to find the target
  # matrix[m][n]
  # while(m < n and n >= 0):
    # if target is in matrix, return 1
    # check to see if target is less than matrix[1][3]
    # if(matrix[m][n] == target):
    #   return 1
    # if the target is less than th
    # else, return 0
    # else:
    #   return 0

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
#print("matrix[-1]: ", matrix[-1])
print(matrix_search(matrix, 55))
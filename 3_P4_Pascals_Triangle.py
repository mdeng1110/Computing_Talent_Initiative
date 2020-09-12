# numRows = int(input())
def pascal_triangle(numRows):
  list = []
  for i in range(numRows):
    if i == 0:
      list.append([1])
    elif i == 1:
      list.append([1,1])
    else:
      newlist = [1]
      prev_row = list[i - 1]
      first_num = prev_row[0]
      for j in range(0, len(prev_row) - 1):
        newlist.append(first_num + prev_row[j + 1])
        first_num = prev_row[j + 1]
      newlist.append(1)
      list.append(newlist)
  return list     
# print(print_pascal(numRows))
  
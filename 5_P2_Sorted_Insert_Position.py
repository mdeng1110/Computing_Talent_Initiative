def find_index(sorted_list, target):
  # return the index if the target is found
  for i in range(len(sorted_list)):
    if sorted_list[i] - target >= 0:
      return i
  return len(sorted_list)
  # else, return the index where it would be if it were
  # inserted in order
  #else:
print(find_index([1,3,5,6], 5))
  
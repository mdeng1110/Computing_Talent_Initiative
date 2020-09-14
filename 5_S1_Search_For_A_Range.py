#array = input()
#target = input()

def first(array, start, end, target, n):
  # if target is in array
  if end >= start:
    mid = (end - start) // 2 + start
    if( ( mid == 0 or target > array[mid - 1]) and array[mid] == target) : 
      return mid 
    elif(target > array[mid]) : 
      return first(array, (mid + 1), end, target, n) 
    else : 
      return first(array, start, (mid - 1), target, n) 
  return -1
def last(array, start, end, target, n):
  if end >= start:
    mid = (end - start) // 2 + start
  #print('MID: ', mid)
    if (( mid == n - 1 or target < array[mid + 1]) and array[mid] == target) : 
      return mid 
    elif (target < array[mid]) : 
      return last(array, start, (mid - 1), target, n) 
    else : 
      return last(array, (mid + 1), end, target, n) 
  return -1
  
def search_for_range(array, target):
  result = []
  start = 0
  end = len(array)
  n = len(array)
  result.append(first(array, 0, n - 1, target, n))
  result.append(last(array, 0, n - 1, target, n))
  return result
print(search_for_range([5, 7, 7, 8, 8, 10], 8))
input_list = [4,5,6,7,0,1,2]

def find_pivot_index(input_list):
  # List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index
  # for current_element_index in range(len(input_list)):
  #   if input_list[current_element_index] < input_list[current_element_index - 1]:
  #     return current_element_index
  # return 0
  start = 0
  end = len(input_list) - 1
  minimum_index = 0
  while start < end-1:
    if end - start % 2 == 0:
      pivot = int((end - start) / 2) + start
    else:
      pivot = int((end - start + 1) / 2) + start
    
    if input_list[pivot] < input_list[minimum_index]:
      end = pivot
      minimum_index = pivot
    else:
      start = pivot
  
  return minimum_index
  
print(find_pivot_index(input_list))
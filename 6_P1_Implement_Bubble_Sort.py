def bubble_sort_swaps(nums):
  swaps = 0
  swapped = True
  last_unsorted_index = len(nums)
  while swapped:
    swapped = False
    for index in range(len(nums) - 1):
      if nums[index] > nums[index + 1]:
        swap_in_place(index, index + 1, nums)
        swaps += 1
        swapped = True
  last_unsorted_index = last_unsorted_index - 1
  print(nums)
  return swaps
  
def swap_in_place(idx1, idx2, input_list):
  input_list[idx1] = input_list[idx1] + input_list[idx2]
  input_list[idx2] = input_list[idx1] - input_list[idx2]
  input_list[idx1] = input_list[idx1] - input_list[idx2]
  
print(bubble_sort_swaps([6, 2, 4, 3]))
# input = unsorted list of integers
# ouput= number of swaps to sort the list
# Google about bubble sort
# Follow the prompt details



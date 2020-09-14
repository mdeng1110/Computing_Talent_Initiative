# input: an array of integers
# output: an integer, how many da operations are needed to sort this array
def da_sort(nums):
  sorted_nums = sorted(nums)
  result = 0
  for i in range(len(nums)):
    if nums[i] == sorted_nums[result]:
      result += 1
  
  return len(nums) - result
  # while nums != sorted_nums:
  #   count = 0
  #   for i in range(len(nums)):
  #     if nums[i] != sorted_nums[i]:
  #       count += 1
  #   index = len(nums) - count
  #   value = nums.pop(index)
  #   nums.append(value)
  #   result += 1
  return result
nums = [1, 5, 2, 4, 3, 6]
print(da_sort(nums))
# count how many integers are out of place
# return that 

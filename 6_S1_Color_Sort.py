def color_sort(nums):
  # nums = [0, 0, 1, 1, 1, 2]
  i = 0
  j = len(nums) - 1
  k = len(nums)
  index = 0
  mid = nums[int(len(nums) / 2) + 1]
  while index < k and i <= index and j >= index:
    if nums[index] == 0:
      nums[index], nums[i] = nums[i], nums[index]
      i = i + 1
    elif nums[index] == 2:
      nums[index], nums[j] = nums[j], nums[index]
      j -= 1
    
    if nums[index] == 1 or i > index:
      index += 1
  
print(color_sort([1,1,0,0,2,1,1,1,0,2,0]))
  
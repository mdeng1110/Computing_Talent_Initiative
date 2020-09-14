# reverses the first k elements of an array
def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]


def pancake_sort(nums):
  k_values = []
  k = len(nums)
  max_index = 0
  while k > 1:
    max_index = nums.index(max(nums[0:k]))
    print('MAX: ', max_index)
    
    if max_index != k:
      if max_index == 0:
          flip(nums, k)
          k_values.append(k)
      else:
        flip(nums, max_index + 1)
        k_values.append(max_index + 1)
        flip(nums, k)
        k_values.append(k)
    k -= 1
      
    # if nums[0] == maximum:
    #   k = j + 1
    # else:
    #   k = nums.index(maximum) + 1
    # flip(nums, k)
    # print('NUMS: ', nums)
    # if nums[j] == maximum:
    #   j -= 1
    # k_values.append(k)
  print(nums)  
  return k_values
  
print(pancake_sort([5, 2, 3, 4, 1]))
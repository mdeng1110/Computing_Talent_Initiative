def merge_sort(nums):
  if len(nums) > 1:
    # bisect the array
    mid = len(nums) // 2
    L = nums[0:mid]
    R = nums[mid:]
    L = merge_sort(L)
    R = merge_sort(R)
    # If these lists are now sorted
    # merge the sorted list
    sorted_list = []
    while len(L) > 0 and len(R) > 0:
      if L[0] > R[0]:
        sorted_list.append(R.pop(0))
      else:
        sorted_list.append(L.pop(0))
    sorted_list.extend(L)
    sorted_list.extend(R)
  else:
    sorted_list = nums
  return sorted_list
  
print(merge_sort([4, 3, 2, 1]))#[x for x in range(0,10)][::-1]))
    
# It divides input array in two halves, 
# calls itself for the two halves and then
# merges the two sorted halves. 
# input = nums
# output = sorted numbers after using merge sort



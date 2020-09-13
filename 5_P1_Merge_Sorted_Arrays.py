def merge_sorted_list(nums1, nums2):
  # modify num1 in-place
  nums1[:] = nums1[0:(len(nums1) - len(nums2))] + nums2
  nums1.sort()
  return nums1
  
print(merge_sorted_list([1,2,3,0,0,0], [2,5,6]))
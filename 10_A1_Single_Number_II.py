def single_number(nums):
  result = 0
  second = 0
  for i in range(len(nums)):
    second |= (result & nums[i])
    result ^= nums[i]
    mask = ~(result & second)
    result &= mask
    second &= mask
  return result
  # Solve for first occurence using XOR  
  # Solve for second occurence by taking the bitwise OR of the second occurence
  # and the bitwise and of nums[i] AND first occurence
  # Solve for the third occurence by bitwise negation of nums[i] and second
  # occurence
  # Remove common occurences of the third occurence in the first occurence using 
  # bitwise AND
  # Remove common occurences of the third occurence in the second occurence using
  # bitwise AND
  # Result should be the first occurence

  # result = nums[0] ^ nums[1]
  # for i in range(2, len(nums)):
  #   result = result ^ nums[i]
  # return result

nums = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
print(single_number(nums)) 
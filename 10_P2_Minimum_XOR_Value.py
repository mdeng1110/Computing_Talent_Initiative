def min_xor_value(num):
  num.sort()
  min_xor = 999999
  val = 0
  for i in range(0, len(num) - 1):
    for j in range(i + 1, len(num) - 1):
      result = num[i] ^ num[j]
      min_xor = min(min_xor, result)
  return min_xor

#print(min_xor_value([0, 2, 3, 5, 8, 8, 9, 23, 37]))
print(min_xor_value([0, 4, 7, 9]))
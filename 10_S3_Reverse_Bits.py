def reverse_bits(n):
  result = 0
  for i in range(32):
    result <<= 1
    result |= n & 1
    n >>= 1
  return result
            
print(reverse_bits(1234))
# def reverse_bits(num):
#   binary = bin(num)
#   reverse = binary[-1:1:-1]
#   return reverse
  
# print(reverse_bits(5))
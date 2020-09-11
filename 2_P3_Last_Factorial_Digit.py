import math
#n = int(input())
def last_factorial_digit(n):
  if n < 0:
    return "Factorial cannot be found for negative numbers"
  elif n == 0:
    return 1
  elif n >= 5:
    return 0
  else:
    m = math.factorial(n)
    if m in [1, 2, 6, 4]:
      return m
    
#print(last_factorial_digit(n))
    
  
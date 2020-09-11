def fast_trailing_zero_factorial(n):
  if n < 5:
    return 0
  elif n >= 5 and n < 25:
    n /= 5 
  else:
    return 6
  return int(n)

#print("Enter number")
#n = input()
#n = int(n)
#print("The number of trailing zeroes is " + str(fast_trailing_zero_factorial(n)))
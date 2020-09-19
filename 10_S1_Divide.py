def divide(dividend, divisor):
  if divisor == 0:
    return 0
  else:
    result = 0
    sign = True
    if dividend < 0 or divisor < 0:
      sign = False
    
    if dividend < 0 and divisor < 0:
      sign = True
      
    dividend = abs(dividend)
    divisor = abs(divisor)
      
    while((dividend - divisor) >= 0):
      count = 0
      while (dividend - (divisor << 1 << count) >= 0):
        count += 1
      result += 1 << count
      dividend -= divisor << count
    
    if not sign:
      return -result
    return result
    
testX = -7
testY = -3
testResult = divide(testX, testY)
print(testResult)
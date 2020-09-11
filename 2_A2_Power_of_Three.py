def power_of_three(n):
    result = 1
    while True:
      result *= 3
      if result == n:
        return True
      elif result > n:
        return False
#n = int(input())
#print(power_of_three(n))
  
# input = positive integer
# return/pringt - output = boolean - true/False
# check if integer is a power of three
# loop - for i in range
# log to get answer
  
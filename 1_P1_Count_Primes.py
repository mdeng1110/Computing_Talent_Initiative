#print("Input number")
#n = int(input())

# Determine if the input number is prime 
def isPrime(n):
  for current_number in range(2,n):
    # if the input number is evenly divisible by the current number?
    if n % current_number == 0:
      return False
  return True

# Determine how many prime numbers are UNDER the input number
def countPrimes(n):
  count = 0 
  for num in range(2,n):
    if isPrime(num):
      count += 1
    
  return count
#print(countPrimes(n))

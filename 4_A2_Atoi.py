def atoi(a):
  #a = a.isalpha
  a = a.strip()
  a = a.replace('\'', '')
  #if numerical number is in range
  if a[0].isalpha():
    return 0
  for s in a:
    if s.isalpha():
      # ignore it
      a = a.replace(s, '') 
  a = int(a)
  if abs(a) > 2147483648:
    return -2147483648
    
  return int(a)

  
print(atoi("   42 is Jackie's number"))
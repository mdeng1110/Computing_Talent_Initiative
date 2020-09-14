# Although you cannot see it, imagine there is a function called isBadVersion already defined.
# the automatic tests will account for it
# here is an example implementation, although the tests will have a different actual value
# the first bad version won't always be 7, but the other function will behave similarly

import math

def isBadVersion(version):
  return version > 7
# when you run your tests, comment this function out.

def firstBadVersion(last_version, isBadVersion):
  start = 1
  end = last_version
  pos = 1
  while start <= end:
    mid = start + (end - start) / 2
    x = isBadVersion(mid)
    if x == True:
      pos = mid
      end = mid - 1
    else:
      start = mid + 1
  y = round(pos)
  
  return y
  
#print(firstBadVersion(4,5))
# haystack = input()
# needle = input()

def strStr(haystack, needle):
  # if needle is an empty string, return 0
  if len(needle) == 0:
    return 0
  return haystack.find(needle)
    
# print(strStr(haystack, needle))
  
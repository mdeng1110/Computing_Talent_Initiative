# s = input()
# t = input()

def valid_anagram(s,t):
  # check to see if the strings are the same length
  # sort the strings alphanumerically
  # compare the strings
  s = list(s)
  t = list(t)
  s.sort()
  t.sort()
  if s == t:
    return True
  else:
    return False
# print(valid_anagram(s, t))
  # create a counter
  # loop to check how many times character appears
  # if both of the words have the same amount of characters that appear then, 
  # return True
  # else, return False
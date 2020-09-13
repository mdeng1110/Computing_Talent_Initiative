#s = input()
def minimumCharacters(s):
  # if (is_palindrome(s)) == True:
  #   return 0
  # else:
    count = 0
    flag = 0
    while len(s) > 0:

      if (is_palindrome(s)):
        flag = 1
        break
      else:
        count += 1
        s = s[:-1]
    if flag:
      return count
        
def is_palindrome(string):
  return string == string[::-1]
# input = string
# output = number of characters that are needed to make the string a palindrome

#print(insert_char(s))
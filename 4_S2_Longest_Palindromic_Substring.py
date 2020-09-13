#input_string = input()
def longest_palindrome(input_string):
  current_string = ''
  max_string = ''
  input_string = input_string.replace(' ', '')
  n = len(input_string)
  print("LENGTH: ", len(input_string))
  print('INPUT_STRING: ', input_string)
  #for each letter in string s, check to see if there is a palindrome
  for i in range(n):
    current_string = input_string[i]
    for j in range(i, n):
      if i == j:
        continue
      print("j: ", j)
      current_string += input_string[j]
      if is_palindrome(current_string):
        if len(max_string) < len(current_string):
          max_string = current_string
  return max_string
def is_palindrome(string):
  return string == string[::-1]
#find the longest palindromic substring in 
print(longest_palindrome('i want to be a racecar driver'))
#input = string
#output = substring that is a longest 
#palindrome
#maximum length of s is 1000
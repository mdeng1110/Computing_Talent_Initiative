import re
#input_str = input()
#input_str = str(input_str)
#input_str = input_str.lower()

def isPalindrome(input_str):
  regexStr=re.sub(r'\W+','', input_str.lower())
  if regexStr == regexStr[::-1]:
    return 1
  else:
    return 0
    
print(isPalindrome("A man, a plan, a canal, Panama."))
# import re
# def isPalindrome(input_str):
# # input should be a string
# # output 1 for true 0 for false
# # convert the output to lowercase
# # remove punctruation and space
#   regexStr=re.sub(r'\W+','', input_str.lower())
#   print(regexStr)
#   print(regexStr[::-1])

# isPalindrome("Race Car")

# def clean_string(dirty_string):
#   cleaned_string=""
#   for element in dirty_string:
#     if element.isalpha():
#       cleaned_string=cleaned_string + element.lower()
#   return cleaned_strin


#name.isalpha()#false    (alphabetic) 

# def isPalindrome(input_str):
#   cleaned_string=clean_string(input_str)
#   if cleaned_string==cleaned_string[::-1]:
#     return 1
#   return 0


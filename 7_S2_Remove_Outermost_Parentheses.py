def removeOuterParentheses(string):
  current_level_count = 0
  output = ""
  for character in string:
    if character == "(":
      # increment the count
      current_level_count += 1
    if current_level_count > 1:
      # add character to the output string
      output += character
    if character == ")":
      # decrement the count
      current_level_count -= 1
  return output

#sampleInput = "(()())(())"
#print(removeOuterParentheses(sampleInput))
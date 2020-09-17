def valid(parentheses):
  parentheses = list(parentheses)
  # if the length of the string is odd, return 0 for False
  if len(parentheses) % 2 == 1:
    return 0
  # create an empty stack
  stack_of_open_paren = []
  for i, paren in enumerate(parentheses):
    if paren in "({[":
      stack_of_open_paren.append(paren)
      # if len(stack_of_open_paren) == 0:
      #   return 0
      if stack_of_open_paren[-1] == "(" and ")" in parentheses:
        if parentheses[i + 1] in "}]":
          return 0
        stack_of_open_paren.pop(-1)
      elif stack_of_open_paren[-1] == "{" and "}" in parentheses:
        if parentheses[i + 1] in ")]":
          return 0
        stack_of_open_paren.pop(-1)
      elif stack_of_open_paren[-1] == "[" and "]" in parentheses:
        if parentheses[i + 1] in ")}":
          return 0
        stack_of_open_paren.pop(-1)

  if len(stack_of_open_paren) == 0:
    return 1
  return 0
# print(valid(["(",")","[","]"]))
print(valid("()"))
    
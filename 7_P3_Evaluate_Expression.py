def evaluate_expression(expression):
  # create empty stack - > stack = []
  stack = []
  # loop over the expression
  for element in expression:
    if element.isnumeric():
      stack.append(int(element))
    else:
      #print('STACK: ', stack)
      if element == "*":
        a = stack.pop()
        b = stack.pop()
        stack.append(b * a)
      elif element == "/":
        a = stack.pop()
        b = stack.pop()
        stack.append(b // a)
      if element == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
      elif element == "-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
      
  return stack.pop(-1)
print(evaluate_expression(["3", "4", "+", "5", "-"]))
print(evaluate_expression(["3", "4", "/", "5", "*"]))
#print(evaluate_expression(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
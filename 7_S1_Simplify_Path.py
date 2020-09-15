def simplifyPath(path):
  stack = []
  for i in path:
    if len(stack) > 0:
      if stack[-1] == '.' and i != '.':
        stack.pop()
      elif i == '.' and stack[-1] == '.':
        for j in range(4):
          if len(stack) > 0:
            stack.pop()
        continue
      
      if i == '/' and stack[-1] == '/':
        stack.pop()
    stack.append(i)
  
  if len(stack) > 1 and stack[-1] == '/':
    stack.pop()
  return ''.join(stack)
# testPath = "/home/"
# testPath = "/a//b////c/d//././/.."
# testPath = "/../"
#testPath = "/home//foo/"
testPath = "/a/./b/../../c/"
testResult = simplifyPath(testPath)
print(testResult)
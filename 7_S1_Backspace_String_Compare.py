def backspaceCompare(String1, String2):
    """
    :type String1: str
    :type String2: str
    :rtype: bool
    """
    stack_1 = []
    for element in String1:
      if element == "#":
        if len(stack_1) == 0:
          pass
        else:
        # remove the last element from the stack
          stack_1.pop(-1)
      else:
        stack_1.append(element)
    String1 = "".join(stack_1)
    
    stack_2 = []
    for element in String2:
      if element == "#":
      # remove the last element from the stack
        if len(stack_2) == 0:
          pass
        else:
          stack_2.pop(-1)
      else:
        stack_2.append(element)
    String2 = "".join(stack_2)
    
    
    if String1 == String2:
      return True
      
    return False
    
sampleInput1A = "a##c"
sampleInput1B = "#a#c"
print(backspaceCompare(sampleInput1A, sampleInput1B))

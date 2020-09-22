def can_finish(num_courses, prerequisites):
  dict = {}
  # for i in range(num_courses):
  for p in prerequisites:
    if p[0] not in dict:
      dict[p[0]] = [p[1]]
    else:
      dict[p[0]].append(p[1])
    
  visited = []
  frontier = [list(dict.keys())[0]]
  
  while frontier:
    node = frontier.pop(0)
    
    if node not in visited:
      visited.append(node)
    else:
      return False
      
    children = dict.get(node)
    
    if children:
      for child in children:
        frontier.append(child)
    
  return True
num_courses = 2
prerequisites = [[1,0], [2, 1], [2, 0]]
print(can_finish(num_courses, prerequisites))
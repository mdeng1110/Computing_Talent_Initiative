### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than has_cycle()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # used in test cases to create cycles in the linked list
  # if you want to test your code without submitting, consider using this function
  def get_reference(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr
      
  # implement this method
  # return true if there is a cycle in this linked list
  def has_cycle(self):
    visited = set()
    current_node = self.head
    while current_node != None:
      if current_node in visited:
        return True
      else:
        visited.add(current_node)
        current_node = current_node.next
    return False
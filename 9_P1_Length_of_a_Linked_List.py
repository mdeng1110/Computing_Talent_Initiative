### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than length()
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
  
  # implement this method
  # return the length of the linked list, an integer value
  def length(self):
    current_node = self.head
    if self.head:
      counter = 0
    else:
      return 0
    while current_node != None:
      counter += 1
      current_node = current_node.next
    return counter
      
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5])
print(ll.length())
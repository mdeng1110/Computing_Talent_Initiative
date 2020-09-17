### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than insert()
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
  
  # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
  def get(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr.data
  
  # implement this method
  def insert(self, data, index):
    tmp = self.head
    node = LinkedNode(data)
    # insert at the beginning of the list
    if index == 0:
      node.next = tmp
      self.head = node
    # insert in the middle of the list
    else:
      count = index - 1
      while count > 0:
        tmp = tmp.next
        count -= 1
      node.next = tmp.next
      tmp.next = node
    # insert at the end of the list
  
  # two arguments = node value, and insert position
ll = LinkedList()
ll.extend([1, 2, 3])
ll.insert(4, 2)
print(ll.get(2))
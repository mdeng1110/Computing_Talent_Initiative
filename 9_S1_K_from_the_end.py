### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
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
  def kth_from_the_end(self, k):
    #result = len(self) - k
    tmp = self.head
    count = 0
    while tmp.next:
      tmp = tmp.next
      count += 1
    index = count - k
    tmp = self.head
    
    while index > 0:
      tmp = tmp.next
      index -= 1
    return tmp.data  

ll = LinkedList()
ll.extend([3,4,5,5,6,7])
print(ll.kth_from_the_end(5))
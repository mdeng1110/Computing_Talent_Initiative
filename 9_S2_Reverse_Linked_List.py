### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
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
  
  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
  def to_array(self):
    array = []
    curr = self.head
    while curr != None:
      array.append(curr.data)
      curr = curr.next
    return array
  
  # implement this method
  def reverse(self):
  ## set current node to head.next
    current = self.head.next
    ## set previous node to head
    previous_node = self.head
    ## set next node to current.next
    next_node = current.next
    
    ## swap head and tail
    self.head = self.tail
    self.tail = previous_node
  
    ## loop through with 3 pointers
    while current != None:
      next_node = current.next ## advance the next node
      current.next = previous_node ## point backwards
      previous_node = current ## advance the previous node 
      current = next_node ## advance the current node
    self.tail.next = None ## terminate the list rather than ending in a cycle
  

my_list = LinkedList()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(21)

my_list.reverse()

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    
  def preorder(self, result=[]):
    if self:
      result.append(self.data)
      if self.left:
        self.left.preorder(result)
      if self.right:
        self.right.preorder(result)
    return result
    
  def postorder(self, result=[]):
    if self:
      if self.left:
        self.left.postorder(result)
      if self.right:
        self.right.postorder(result)
      result.append(self.data)
    return result
    
  def inorder(self, result=[]):
    if self:
      if self.left:
        self.left.inorder(result)
      result.append(self.data)
      if self.right:
        self.right.inorder(result)
    return result
    
class Tree:
  def __init__(self):
    self.root = None
    
    
  def level_order_traversal(self):
    # return the tree as a list in a level-order sequence
    q = []
    q.append(self.root.data)
    q.append(self.root.left.data)
    q.append(self.root.right.data)
    d_1 = tree.root.left
    q.append(d_1.left.data)
    q.append(d_1.right.data)
    return q
    
  def pre_order_traversal(self):
    # return the tree as a list in a pre-order sequence (dfs)
    return self.root.preorder()
    
  def in_order_traversal(self):
    # return the tree as a list in-order (dfs)
    return self.root.inorder()
    
  def post_order_traversal(self):
    # return the tree as a list in a post-order sequence (dfs)
    return self.root.postorder()
    
tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)

# print(tree.pre_order_traversal())
# print(tree.post_order_traversal())
#print(tree.in_order_traversal())
print(tree.level_order_traversal())

# d_0 = tree.root
# print(d_0.data)
# print(d_0.left.data, d_0.right.data)
# d_1 = tree.root.left
# print(d_1.left.data, d_1.right.data)
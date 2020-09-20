class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None

  def print_bfs(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      print(current_node.data)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

  def in_order_traversal(self):
    nodes = []
    def dfs(node):
      if node:
        
        dfs(node.left)
        nodes.append(node.data)
        dfs(node.right)

        
    dfs(self.root)
    return nodes
    
  def add(self,node):
    if self.root is None:
      self.root = node
    else:
      def insert(root, node):
        if node.data < root.data:
          if root.left is None:
            root.left = node
          else:
            insert(root.left, node)
        else:
          if root.right is None:
            root.right = node
          else:
            insert(root.right,node)
      root = self.root
      insert(root, node)
tree = Tree()
tree.root = Node(55)

tree.root.left = Node(20)
tree.root.right = Node(100)

tree.root.left.left = Node(15)
tree.root.left.right = Node(30)

tree.root.right.left = Node(60)
tree.root.right.right = Node(200)

print(tree.add(Node(7)))
print(tree.in_order_traversal())

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 999

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min:
          self.stack.append(self.min)
          self.min = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
          tmp = self.stack[-1]
          self.stack.pop()
          if self.min == tmp:
            self.min = self.top()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
          return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.min
        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
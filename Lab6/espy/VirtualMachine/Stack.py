class Stack:
  '''
  It represents the stack of the virtual machine.
  '''
  def __init__(self):
    self.stack = []
  
  def pop(self):
    '''
    Remove the top element of the stack
    '''
    v = self.stack[-1]
    self.stack.pop()
    return v
  
  def push(self, v):
    '''
    Push a value v on the top of the stack
    '''
    self.stack.append(v)

  def swap(self):
    '''
    Swap the top element of the stack with the one bellow
    '''
    a = self.pop()
    b = self.pop()
    self.stack.append(a)
    self.stack.append(b)
  
  def dup(self):
    '''
    Duplicate the top element of the stack
    '''
    self.stack.append(self.stack[-1])

  def size(self):
    '''
    Return the number of elements in the stack
    '''
    return len(self.stack)

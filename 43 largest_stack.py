# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:15:56 2017

@author: harrisot
"""

class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]
      
class MaxStack:
  def __init__(self):
    self.stack = Stack()
    self.max_stack = Stack()
    
  def push(self, item):
    self.stack.push(item)
    
    if self.max_stack.peek() is None or item > self.max_stack.peek():
      self.max_stack.push(item)
      
  def pop(self):
    item = self.stack.pop()
    if item == self.max_stack.peek():
      self.max_stack.pop()
    return item
    
  def get_max(self):
    return self.max_stack.peek()
  
  
mystack = MaxStack()
mystack.push(11)
mystack.push(2)
mystack.push(30)
mystack.push(44)

print(mystack.stack.items)
print(mystack.max_stack.items)
    
    
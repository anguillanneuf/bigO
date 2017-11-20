# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:43:55 2017

@author: harrisot

Image two stacks for this question. 
"""

class Queue:
  def __init__(self):
    self.in_stack = []
    self.out_stack = []
    
  def enqueue(self, item):
    self.in_stack.append(item)
  
  def dequeue(self):
    if len(self.out_stack) == 0:
      while len(self.in_stack)>0:
        x = self.in_stack.pop()
        self.out_stack.append(x)
      if len(self.out_stack)==0:
        raise IndentationError("Empty queue!")
      
    return self.out_stack.pop()
  
  
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.out_stack)
print(queue.in_stack)


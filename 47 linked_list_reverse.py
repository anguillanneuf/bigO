# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:32:27 2017

@author: harrisot
"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse_linked_list(root):
  old = None
  while root.next is not None:
    
    new = root.next
    root.next = old
    old = root
    root = new
    
  if root.next is None:
    root.next = old
    
        
a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

reverse_linked_list(a)
print(c.next.value)
print(b.next.value)
print(a.next)
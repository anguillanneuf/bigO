# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:57:02 2017

@author: harrisot

     a b c b
fast     ^
slow     ^
"""

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
        
def check_cycles(root):
  fast = root
  slow = root
  
  while fast.next and fast:
    slow = slow.next
    fast = fast.next.next
    if fast == slow:
      return True
  return False
    
a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c
c.next = b

print(check_cycles(a))
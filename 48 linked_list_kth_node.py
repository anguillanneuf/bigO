# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:32:08 2017

@author: harrisot
"""

class LinkedListNode:

  def __init__(self, value):
      self.value = value
      self.next  = None

def kth_to_last_node(k, root):
  start_node = root
  end_node = root
  
  for i in range(k-1):
    if end_node.next is None:
      raise ValueError("{} is larger than linked list!".format(k))
    end_node = end_node.next
    
  while end_node.next:
    start_node = start_node.next
    end_node = end_node.next

  return start_node.value

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last_node(2, a))
# returns the node with value "Devil's Food" (the 2nd to last node)
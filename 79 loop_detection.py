#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:30:01 2017

@author: tz
"""

class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None
    
def loop_detection(node):
  slow = node
  fast = node.next.next

  # fast catches up with slow
  while slow.value != fast.value:
    slow = slow.next
    fast = fast.next.next
  # length of the cycle
  count = 1
  curr = slow
  mem = curr.value
  while mem != curr.next.value:
    curr = curr.next
    count += 1
  # prepare two pointers
  p1 = node
  p2 = node
  for _ in range(count):
    p2 = p2.next
  # find beginning of the cycle
  while p1.value != p2.value:
    p1 = p1.next
    p2 = p2.next
  
  return p1.value
  
  
a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

print(loop_detection(a))
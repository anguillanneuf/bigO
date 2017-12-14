#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:42:33 2017

@author: tz
"""
class LinkedListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

def palindrome(node):
  slow = node
  fast =  node
  left = []
  
  while fast.next and fast.next.next:
    left.append(slow.value)
    slow = slow.next
    fast = fast.next.next

  while len(left)>0:
    slow = slow.next
    curr = left.pop()
    if curr != slow.value:
      return False
     
  return True

a = LinkedListNode('R')
b = LinkedListNode('O')
c = LinkedListNode('N')
d = LinkedListNode('N')
e = LinkedListNode('Y')
f = LinkedListNode('N')
g = LinkedListNode('O')
h = LinkedListNode('R')

a.next = b
b.next = c
c.next = d
d.next = e

print(palindrome(a))

a.next = b
b.next = c
c.next = d
d.next = f
f.next = g
g.next = h

print(palindrome(a))
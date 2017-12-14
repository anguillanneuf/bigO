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
  arr = []
  while node:
    arr.append(node.value)
    node = node.next
  i = 0
  j = len(arr)-1
  while i<j:
    if arr[i]!=arr[j]:
      return False
    i+=1
    j-=1
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
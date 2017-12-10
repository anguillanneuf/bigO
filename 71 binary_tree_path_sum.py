#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:41:03 2017

@author: tz
"""
class Global():
  globalmax = -float('inf')

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
  def largest_path(self, node):
    """Find the path that sums to the largest value by adding
    all the node values along the way. O(n) time, O(n) space"""
    
    if node.left is None and node.right is None:
      temp = max(0, node.value)
      if temp > Global.globalmax:
        Global.globalmax = temp
      return temp
    
    left = right = 0
    
    if node.left:
      left = self.largest_path(node.left)
      
    if node.right:
      right = self.largest_path(node.right)
      
    Global.globalmax = max(Global.globalmax, 
                           left, 
                           right, 
                           left+node.value, 
                           left+node.value+right, 
                           node.value+right)
    
    return max(left+node.value, node.value, node.value+right)
  
# Test 1
root = Node(3)
root.left = Node(-1)
root.left.left = Node(100)
root.left.right = Node(-9)
root.right = Node(98)

root.largest_path(root)
print("Example 1: max path sum (200) is ", Global.globalmax)

# Test 2
a = Node(-10)
b = Node(2)
c = Node(10)
d = Node(20)
e = Node(1)
f = Node(-25)
g = Node(3)
h = Node(4)
a.left, a.right = b, c
b.left, b.right = d, e
c.left, c.right = None, f
f.left, f.right = g, h

Global.globalmax = -float('inf') # reset Global var
a.largest_path(a)
print ("Example 2: max path sum (23) is ", Global.globalmax)
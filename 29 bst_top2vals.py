# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:14:04 2017

@author: harrisot
"""

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
    
    def find_top_2(self):
        top2 = []
        stack = []
        
        stack.append(self)
        
        while len(stack) > 0:
            curr = stack.pop()
            top2.append(curr.value)
            top2 = sorted(top2)[::-1][:2]
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
        return top2
    
    def find_top2_fast(self):
        stack = []
        stack.append(self)
        top2 = []
        top2.append(self.value)
        
        while len(stack) > 0:
            curr = stack.pop()
            top2.append(curr.value)
            top2 = sorted(top2)[::-1][:2]
            if curr.right:
                stack.append(curr.right)
            elif curr.left:
                stack.append(curr.left)
        return top2
    

def find_largest(node):
    while node.right:
        node = node.right
    return node.value
        

def find_second_largest_recursive(node):

    if (not node.right) and node.left:
        return find_largest(node.left)
        
    if node.right and not node.right.left and not node.right.right:
        return node.value
    else:
        return find_second_largest_recursive(node.right)
        
def find_second_largest_iterative(node):
    curr = node
    while curr: 
        if not curr.right and curr.left:
            return find_largest(curr.left)
        
        if curr.right and (not curr.right.left) and (not curr.right.right):
            return curr.value
        
        curr = curr.right
        
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(4)
bt.right.insert_right(16)

print(bt.find_top_2())
print(bt.find_top2_fast())
print(find_largest(bt))
print(find_second_largest_recursive(bt))
print(find_second_largest_iterative(bt))
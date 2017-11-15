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
    

    def find_largest(self, node):
        while node.right:
            node = node.right
        return node.value
        

    def find_second_largest(self, node):

        if (not node.right) and node.left:
            ans = self.find_largest(node.left)
            return ans
            
        if node.right and not node.right.left and not node.right.right:
            return node.value
        else:
            temp = self.find_second_largest(node.right)
            if temp > self.value:
                return temp
            else:
                return self.value
        
        
   
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(4)
bt.right.insert_left(6)

print(bt.find_top_2())
print(bt.find_top2_fast())
print(bt.find_largest(bt))
print(bt.find_second_largest(bt))
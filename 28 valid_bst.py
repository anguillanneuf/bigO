# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:27:35 2017

@author: harrisot
"""

class BinaryTreeNode:
    """
    BST are great for quick lookups. O(logN) time.
    """

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
    
    def check_binary_search_tree_efficient(self):
        stack = []
        stack.append((self, -float('inf'), float('inf')))
        
        while len(stack) > 0: 
            v, max_left, min_right = stack.pop()
            
            if v.value < max_left or v.value > min_right: 
                return False
            
            if v.left:
                stack.append((v.left, max_left, v.value))
            if v.right:
                stack.append((v.right, v.value, min_right))
                
        return True
    
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(4)

print(bt.check_binary_search_tree_efficient())
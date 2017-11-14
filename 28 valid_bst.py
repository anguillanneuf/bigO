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
    
    def check_binary_search_tree_iterative(self):
        stack = []
        stack.append((self, -float('inf'), float('inf')))
        
        while len(stack) > 0: 
            v, lbound, ubound = stack.pop()
            
            if v.value < lbound or v.value > ubound: 
                return False
            
            if v.left:
                stack.append((v.left, lbound, v.value))
            if v.right:
                stack.append((v.right, v.value, ubound))
                
        return True

    
    def check_bst_recursive(self, node, lower, upper):
        if not node:
            return True
        
        if node.value <= lower or node.value >= upper:
            return False
                
        return self.check_bst_recursive(node.left, lower, node.value) and \
                self.check_bst_recursive(node.right, node.value, upper)
    
    
    
bt = BinaryTreeNode(5)
bt.insert_left(3)
bt.insert_right(7)
bt.left.insert_left(1)
bt.left.insert_right(9)

print(bt.check_binary_search_tree_iterative())
print(bt.check_bst_recursive(bt, -float('inf'), float('inf')))
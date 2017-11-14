# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:58:45 2017

@author: harrisot

A tree is "superbalanced" if the difference between the depths of 
any two leaf nodes is no greater than one.

"""
from collections import deque
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
    
    def check_super_balanced(self):
        """
        1. BFS
        2. Update queue that stores nodes to visit
        3. Pop nodes as I visit them, if they are leaves, save to leaves
        """
        leaf_levels = []
        queue = deque()
        queue.append((self, 0))
        
        while queue:
            curr_node, level = queue.popleft()
            if curr_node.left: 
                queue.append((curr_node.left, level+1))
            if curr_node.right:
                queue.append((curr_node.right, level+1))
            
            if (not curr_node.left) and (not curr_node.right):
                leaf_levels.append(level)
                if len(set(leaf_levels)) > 2:
                    return False
        return True
    
bt = BinaryTreeNode(1)
bt.insert_left(BinaryTreeNode(2))
bt.insert_right(BinaryTreeNode(3))
bt.left.insert_left(4)
bt.left.insert_right(5)
bt.left.left.insert_left(6)

print(bt.check_super_balanced())
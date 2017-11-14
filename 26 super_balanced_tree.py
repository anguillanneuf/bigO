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
    
    def check_super_balance_bfs(self):
        """
        1. BFS
        2. Update queue that stores nodes to visit
        3. Pop nodes as I visit them, if they are leaves, save to leaves
        """
        depths = []
        queue = deque()
        queue.append((self, 0))
        
        while queue:
            curr, level = queue.popleft()
            if curr.left: 
                queue.append((curr.left, level+1))
            if curr.right:
                queue.append((curr.right, level+1))
            
            if (not curr.left) and (not curr.right):
                depths.append(level)
                if len(set(depths)) > 2 or \
                    (len(set(depths))==2 and abs(depths[0]-depths[1])>1):
                    return False
        return True
    
    def check_super_balance_dfs(self):
        """
        1. DFS
        2. Update stack that stores nodes to visit. 
           len(stack) <= max_depth
        3. Check for super balance
        """
        stack = []
        stack.append((self, 0))
        depths = []
        
        while len(stack) > 0:
            curr, depth = stack[-1]
            del stack[-1]
            
            if curr.left:
                stack.append((curr.left, depth+1))
            if curr.right:
                stack.append((curr.right, depth+1))
        
            if (not curr.left) and (not curr.right):
                depths.append(depth)
                if len(set(depths)) > 2 or \
                    (len(set(depths))==2 and abs(depths[0]-depths[1])>1):
                    return False
        return True
    
bt = BinaryTreeNode(1)
bt.insert_left(BinaryTreeNode(2))
bt.insert_right(BinaryTreeNode(3))
bt.left.insert_left(4)
bt.left.insert_right(5)
bt.left.left.insert_left(6)

print(bt.check_super_balance_bfs())
print(bt.check_super_balance_dfs())
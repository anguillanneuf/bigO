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
    
    def check_binary_search_tree(self):
        """
        max(left) < node
        min(right) > node
        DFS, update max_left, min_right
        """

        stack = []
        stack.append(self.left.value)
        max_left = stack[-1].value

        while len(stack) > 0:
            curr = stack[-1]
            stack.pop()
            if curr.value > max_left:
                max_left = curr.value
            if curr.left:
                stack.append(curr.left.value)
            if curr.right:
                stack.append(curr.right.value)
            if max_left > self.value:
                return False
            
        stack = []
        stack.append(self.right.value)
        min_right = stack[-1].value
        while len(stack) > 0:
            curr = stack[-1]
            stack.pop()
            if curr.value < min_right:
                min_right = curr.value
            if curr.left:
                stack.append(curr.left.value)
            if curr.right:
                stack.append(curr.right.value)
            if min_right < self.value:
                return False
        
        return True
    
bt = BinaryTreeNode(1)
bt.insert_left(BinaryTreeNode(2))
bt.insert_right(BinaryTreeNode(3))
bt.left.insert_left(4)
bt.left.insert_right(5)
bt.left.left.insert_left(6)

print(bt.check_binary_search_tree())
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:16:02 2017

@author: harrisot
"""
from collections import deque

class BinaryTreeNode:
    """
    BST are great for quick lookups. O(logN) time.
    """

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
        self.wrong1 = None
        self.wrong2 = None
        
    def in_order(self, node):
      if node:
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)
        
    def in_order_dst(self, node, triple):
      if node:
        self.in_order_dst(node.left, triple)
        triple.append(node)
        if len(triple) == 3:
          self.check_triple(triple)
        self.in_order_dst(node.right, triple)

    def check_triple(self, triple):
      if self.wrong1 and self.wrong2:
        self.wrong1.value, self.wrong2.value = self.wrong2.value, self.wrong1.value
      elif triple[0].value <= triple[1].value <= triple[2].value:
        return
      elif triple[0].value >= triple[1].value >= triple[2].value:
        self.wrong1 = triple[0]
        self.wrong2 = triple[1]
      elif self.wrong1 is None:
        if triple[0].value >= triple[1].value:
          self.wrong1 = triple[0]
        elif triple[1].value >= triple[2].value:
          self.wrong1 = triple[1]
      elif self.wrong2 is None:
        if self.wrong1.value <= triple[1].value <= triple[2].value:
          self.wrong2 = triple[0]
        elif triple[0].value <= self.wrong1.value <= triple[2].value:
          self.wrong2 = triple[1]
        elif triple[0].value <= triple[1].value <= self.wrong1.value:
          self.wrong2 = triple[2]

bt = BinaryTreeNode(7)
bt.left = BinaryTreeNode(4)
bt.left.left = BinaryTreeNode(1)
bt.left.right = BinaryTreeNode(5)
bt.right = BinaryTreeNode(11)

triple = deque(maxlen=3)
triple.append(BinaryTreeNode(-float('inf')))
bt.value, bt.left.left.value = bt.left.left.value, bt.value
bt.in_order(bt)
bt.in_order_dst(bt, triple)
bt.in_order(bt)
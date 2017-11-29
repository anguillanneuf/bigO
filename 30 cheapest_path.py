# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:30:28 2017

@author: harrisot

Pramp question
"""
import sys

class Node: 
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parents = None
       
def get_cheapest_cost_recursive(node):
    if len(node.children) == 0:
        return node.cost
    else:
        temp = sys.maxsize
        for child in node.children:
            temp = min(temp, get_cheapest_cost_recursive(child))
        return temp + node.cost
    
def get_cheapest_cost_iterative(node):
    minCost = sys.maxsize
    stack = []
    stack.append((node, node.cost))
    
    while len(stack) > 0:
        node_i, carry = stack.pop()
        if len(node_i.children) == 0:
            if carry < minCost:
                minCost = carry
        else:
            for child in node_i.children:
                stack.append((child, carry + child.cost))       
    
    return minCost
    
tree = Node(0)
tree.children = [Node(5), Node(3), Node(6)]
tree.children[0].children = [Node(4)]
tree.children[1].children = [Node(2), Node(0)]
tree.children[2].children = [Node(1), Node(5)]
tree.children[1].children[0].children = [Node(1)]
tree.children[1].children[0].children[0].children = [Node(1)]
tree.children[1].children[1].children = [Node(10)]

print(get_cheapest_cost_recursive(tree))
print(get_cheapest_cost_iterative(tree))
        

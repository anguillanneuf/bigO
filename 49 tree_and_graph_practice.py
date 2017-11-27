#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:43:50 2017

@author: tz
"""
import heapq

def convert_arr_to_bst_with_min_height(in_arr, out_arr = []):
    if len(in_arr) <= 2: 
        for i in in_arr: 
            out_arr.append(i)
    else: 
        mid = len(in_arr)//2
        out_arr.append(in_arr[mid])
        convert_arr_to_bst_with_min_height(in_arr[:mid], out_arr)
        convert_arr_to_bst_with_min_height(in_arr[mid+1:], out_arr) 

output = []
convert_arr_to_bst_with_min_height([1,2,3,4,5,6,7], output)
print(output)

class BinaryTreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        
class LinkedList:
    def __init__(self, v):
        self.value = v
        self.next = None

def linked_list_of_depths(root):
    stack = []
    stack.append((0, root))
    mymap = dict()
    
    while len(stack) > 0: 
        depth, node = stack.pop()
        if depth not in mymap.keys():
            mymap.update({depth: LinkedList(node.value)})
        else:
            
            curr = mymap.get(depth)
            while curr.next: 
                curr = curr.next
            curr.next = LinkedList(node.value)

        if node.left: 
            stack.append((depth+1, node.left))
        if node.right:
            stack.append((depth+1, node.right))
    
    return mymap

bt = BinaryTreeNode(3)
bt.left = BinaryTreeNode(1)
bt.left.right = BinaryTreeNode(2)
bt.right = BinaryTreeNode(4)
bt.right.right = BinaryTreeNode(5)

print(linked_list_of_depths(bt).get(1).next.value)



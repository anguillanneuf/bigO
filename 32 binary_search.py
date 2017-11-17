# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 13:52:29 2017

@author: harrisot
"""

class Trie:
    def __init__(self):
        self.rootNode = {}
        
    def search_and_expand(self, x):
        is_there = True
        curr = self.rootNode
        
        for i in list(str(x)):
            if i not in curr:
                is_there = False
                curr[i] = {}
            curr = curr[i]
            
        if '*' not in curr:
            is_there = False
            curr['*'] = {}
                
        return is_there

def find_int_in_ordered_list(ints, x):
    trie = Trie()
    for i in ints:
        is_there = trie.search_and_expand(i)

    is_there = trie.search_and_expand(x)
    return is_there

def find_num_in_ordered_list(ints, x):
    if len(ints) < 1:
        return False
    
    if len(ints) == 1:
        return True if ints[0]==x else False
        
    mid = len(ints)//2
    
    if ints[mid] == x:
        return True
    
    if ints[mid] < x:
        return find_num_in_ordered_list(ints[mid+1:],x)
    else:
        return find_num_in_ordered_list(ints[:mid],x)

print(find_int_in_ordered_list([1,12,123,22,23,9,987], 98))
print(find_num_in_ordered_list([1,12,123,22,23,9,987], 98))
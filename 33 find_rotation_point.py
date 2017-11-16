# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:22:46 2017

@author: harrisot
"""
def compare(a, b):
    i = 0
    while i < len(b):
        if i >= len(a): return False
        if ord(a[i]) > ord(b[i]): return True
        if ord(a[i]) < ord(b[i]): return False
        
        i += 1

def find_rot_pt(words):
    if len(words) < 1:
        return -1
    i = 1
    while i < len(words):
        if compare(words[i-1], words[i]):
            return i
        else: i += 1
    return -1

def find_rotation_point(words):
    lower, upper = 0, len(words)-1
    
    while lower < upper:
        
        if lower + 1 == upper:
            return upper if upper != 1 else -1
        
        mid = (lower + upper)//2 
        
        if words[mid] < words[upper]: 
            upper = mid
        else:
            lower = mid

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate', 
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage'
]

print(find_rot_pt(words))
print(find_rotation_point(words))
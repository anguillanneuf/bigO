#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:02:15 2018

@author: tz
"""

def hoppable_towers(arr):
    stash = []
    
    stash.append(0)
    
    while stash:
        pos = stash.pop()
        if pos >= len(arr):
            return True
        steps = arr[pos]
        for i in range(1, steps+1):
            stash.append(pos+i)
        
    return False

print(hoppable_towers([1,0])) # False
print(hoppable_towers([4,2,0,0,2,0])) # True
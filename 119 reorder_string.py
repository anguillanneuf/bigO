#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:45:31 2018

@author: tz

Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

"""

def reorder_string(s):
    
    mem = dict()
    for c in s:
        if c in mem:
            mem[c]+=1
        else:
            mem.setdefault(c,1)

    output = ''
    prev_key = None
    
    while mem:
        
        max_key = max(mem, key=mem.get) # max(mem.items, key=operator.itemgetter(1))
        max_val = mem[max_key]
        
        if max_val - 1 > (sum(mem.values())-max_val):
            break
        
        if max_key == prev_key:         # get the next key with the highest val
            max_val = mem.pop(max_key)
            curr_key = max(mem, key=mem.get)
            mem.update({max_key: max_val})
        else:
            curr_key = max_key

        output += curr_key
        mem[curr_key] -= 1
        prev_key = curr_key

        if mem[curr_key]==0:
            mem.pop(curr_key)
 
    return output

print(reorder_string('bbbbb'))
print(reorder_string('vvvlo'))


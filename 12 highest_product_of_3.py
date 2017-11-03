#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:47:49 2017

@author: tz
"""

def highest_product_of_3(ints):
    highest_3 = sorted(ints[:3])
    pos = sorted([i for i in highest_3 if i > 0])
    neg = sorted([i for i in highest_3 if i < 0])
    
    for i in range(3, len(ints)):
        if ints[i] > 0 and ints[i] > min(pos):
            if len(pos) == 3:
                pos.pop(0)
            pos.append(ints[i])
            pos = sorted(pos)
            
        if ints[i] < 0 and ints[i] < max(neg):
            if len(neg) == 3:
                neg.pop(2)
            neg.append(ints[i])
            neg = sorted(neg)
            
    highest_product = 1
    if len(pos) >=3:
        highest_product = pos[0] * pos[1] * pos[2]
    if len(neg) >=2:
        temp = neg[0]*neg[1]*pos[2]
        if temp > highest_product:
            highest_product = temp
    
    return highest_product

ints = [-10, -10, 1, 3, 2] #[2,4,6,0,9,3,6]
print(highest_product_of_3(ints))

#==============================================================================
# Reflection:
# Why doesn't my solution look elegant? How could I have done better?
# Perhaps I could have considered making `pos` and `neg` of length 2.
# Instead of keeping a list, keep a running product.
# Instead of thinking in terms of pos/neg, perhaps lowest/highest works.
#==============================================================================

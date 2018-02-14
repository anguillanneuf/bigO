#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:01:35 2018

@author: tz
"""

def collect_rainwater(arr):
    
    unit = 0
    
    if len(arr)<3: return unit
    
    k = 1
    original = arr.copy()
    
    while k + 1 < len(original):
        
        if arr[k-1] < arr[k]:
            k += 1
        else:
            i = k+1
            peak = max(arr[i:])
            j = i + arr[i:].index(peak)
            arr[k:j] = [peak]*(j-k)
            k = j
            
    print(original)
    print(arr)
            
    for k in range(len(original)):
        unit += arr[k]-original[k]
    
    return unit


arr = [1,4,1,2,3,3,2,3,0,2]
arr = [1,2,3,1,4]
print(collect_rainwater(arr))
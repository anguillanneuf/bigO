#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:01:35 2018

@author: tz
"""

def collect_rainwater(arr):
    
    unit = 0
    
    if len(arr)<3: return unit
    
    i = 1
    original = arr.copy()
    
    while i < len(original):
        
        if arr[i-1] < arr[i]:
            i += 1
        else:
            peak = max(arr[i:])
            j = i + arr[i:].index(peak)
            arr[i:j+1] = [peak]*(j+1-i)
            i = j+1

    for i in range(len(original)):
        unit += arr[i]-original[i]
    
    return unit


arr = [1,4,1,2,3,1,2,3,0,2]
print(collect_rainwater(arr))
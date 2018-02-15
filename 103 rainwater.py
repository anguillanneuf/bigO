#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:01:35 2018

@author: tz

https://leetcode.com/problems/trapping-rain-water/description/
"""

def collect_rainwater(arr):
    
    unit = 0
    if len(arr)<3:
        return unit
    
    i = 0 
    j = len(arr)-1
    lmax = None
    rmax = None
    
    while i<j: 
        lmax = max(arr[i], lmax) if lmax else arr[i]
        rmax = max(arr[j], rmax) if rmax else arr[j]
        if lmax > rmax:
            unit += rmax - arr[j]
            j-=1
        else:
            unit += lmax - arr[i]
            i+=1
    
    return unit


arr = [1,4,1,2,3,3,2,3,0,2]
#arr = [1,2,3,1,4]
#arr = [2,1,0,2]
print(collect_rainwater(arr))
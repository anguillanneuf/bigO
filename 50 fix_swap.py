#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 22:14:25 2017

@author: tz
"""

def fix_swap(arr):
    
    wrong1 = None
    wrong2 = None
    
    for i in range(len(arr)):
        
        left = arr[i-1] if i>0 else -float('inf')
        right = arr[i+1] if i+1 < len(arr) else float('inf')
        
        if wrong1 is not None and wrong2 is not None:
            break
        elif left <= arr[i] and arr[i] <= right: 
            continue
        elif left >= arr[i] and arr[i] >= right and i >0:
            wrong1 = i-1
            wrong2 = i+1
        elif wrong1 is None:
            if left >= arr[i]:
                wrong1 = i-1
            elif arr[i] >= right:
                wrong1 = i
        elif wrong2 is None:
            if arr[wrong1] <= arr[i] and arr[i] <= right:
                wrong2 = i-1
            elif left <= arr[wrong1] and arr[wrong1] <= right:
                wrong2 = i
            elif left <= arr[i] and arr[i] <= arr[wrong1]:
                wrong2 = i+1

    arr[wrong1], arr[wrong2] = arr[wrong2], arr[wrong1]
    
    return arr

print(fix_swap([2,1,3,4,5]))
print(fix_swap([3,2,1,4,5]))
print(fix_swap([4,2,3,1,5]))
print(fix_swap([5,2,3,4,1]))

print(fix_swap([1,3,2,4,5]))
print(fix_swap([1,4,3,2,5]))
print(fix_swap([1,5,3,4,2]))

print(fix_swap([1,2,4,3,5]))
print(fix_swap([1,2,5,4,3]))
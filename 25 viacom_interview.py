# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:46:30 2017

@author: harrisot

David interviews his engineers with this question.

input:
---
[1, 4, 6]
[2, 7]

output:
---
[1, 7, 3]
"""

arr1 = [9, 9, 7]
arr2 = [4, 6]

from collections import deque

def sum_two_arrays(arr1, arr2):
    n = max(len(arr1), len(arr2))
    arr = deque([0] * n)
    
    for i in range(n-1, -1, -1):
        a = arr1[i - n + len(arr1)] if i - n + len(arr1) >= 0 else 0
        b = arr2[i - n + len(arr2)] if i - n + len(arr2) >= 0 else 0
        
        temp = arr[i] + a + b
        arr[i] = temp % 10 
        
        if i > 0: 
            arr[i-1] += temp//10
        elif temp//10:
            arr.appendleft(1)

    return arr

print(sum_two_arrays(arr1, arr2))
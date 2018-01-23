#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 21:08:44 2018

@author: tz
"""

def sum_of_zero(arr):
    n = len(arr)
    
    for i in range(n):
        
        for j in range(i, n):
            
            if sum(arr[i:j+1])==0:
                print(arr[i:j+1])
    return 



arr = [6, 4, -3, -1, -6, 0, 6]

print("First approach")
sum_of_zero(arr)

def zero_sums(arr):
    k = 0
    mem = [0 for _ in range(len(arr)+1)]
    
    while k < len(arr): 
        mem.pop()     
        for i in range(len(mem)):
            mem[i] += arr[k+i]
            if mem[i] == 0: 
                print(arr[i:k+i+1])
        k += 1
print("Second approach")
zero_sums(arr)
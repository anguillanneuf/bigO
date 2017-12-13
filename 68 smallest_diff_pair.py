#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:11:13 2017

@author: tz
"""

def smallest_diff_pair(arr1, arr2):
  m = len(arr1)
  n = len(arr2)
  if m > n: arr1, arr2 = arr2, arr1
  diff = float('inf')
  
  arr2 = [-float('inf')]+sorted(arr2)+[float('inf')]
  
  for i in range(len(arr1)):
      
    lo = 0
    hi = len(arr2)-1
    
    while lo< hi:
      mid = (lo + hi)//2
      if arr1[i] < arr2[mid]:
        hi = mid
      else:
        lo = mid+1
    
    if lo==1:
      diff = min(diff, abs(arr1[i]-arr2[lo]))
    elif lo==len(arr2):
      diff = min(diff, abs(arr1[i]-arr2[lo-1]))
    else: 
      diff = min(diff, abs(arr1[i]-arr2[lo]), abs(arr2[lo-1]-arr1[i]))
    
  return diff 

arr1 = [1,3,15,11,2]
arr2 = [23,127,235,19,8]

print(smallest_diff_pair(arr1, arr2))
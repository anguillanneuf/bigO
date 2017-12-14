#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 18:11:13 2017

@author: tz
"""

def smallest_diff_pair(arr1, arr2):
  diff = float('inf')
  i = j = 0
  arr1 = sorted(arr1)
  arr2 = sorted(arr2)
  while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
      diff = min(diff, abs(arr1[i]-arr2[j]))
      i+=1
    else:
      diff = min(diff, abs(arr1[i]-arr2[j]))
      j+=1
    
  return diff 

arr1 = [1,3,15,11,2]
arr2 = [23,127,235,19,8]

print(smallest_diff_pair(arr1, arr2))
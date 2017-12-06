#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:50:28 2017

@author: tz
"""

def merge_sorted_lists(arr1, arr2):
  i = j = 0
  n = len(arr1)
  m = len(arr2)
  arr = []
  
  while i < n:
    if arr1[i] < arr2[j]:
      arr.append(arr1[i])
      i += 1
    else:
      arr.append(arr2[j])
      j += 1
      
  while j < m:
    arr.append(arr2[j])
    j += 1
  
  return arr



my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print(merge_sorted_lists(my_list, alices_list))
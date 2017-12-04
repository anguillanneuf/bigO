#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:57:08 2017

@author: tz
"""

def find_dups_beast_mode(arr):
  """Beast mode
  1. find cycle
  2. calculate length of the cycle
  3. get into cycle
  4. find the beginning or end of the cycle"""
  
  n = len(arr)
  curr = n
  
  # Step 1
  for _ in range(n-1):
    curr = arr[curr-1]
    
  mark = curr
  pointer = arr[curr-1]
  count = 1
  
  # Step 2
  while mark != pointer:
    pointer = arr[pointer-1]
    count += 1
  print("Length of the cycle: {}".format(count))
  
  i = n
  j = n
  # Step 3
  for _ in range(count):
    i = arr[i-1]
z
  # Step 4
  while i!=j:
    print(i,j)
    i = arr[i-1]
    j = arr[j-1]
    
  return i


print(find_dups_beast_mode([1,3,2,1,3]))
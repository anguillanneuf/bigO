#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:57:08 2017

@author: tz
"""

def find_dups_beast_mode(arr):
  # find cycle
  n = len(arr)
  curr = n # if starting at 0, there will be a problem 
  
  for _ in range(n):
    curr = arr[curr-1]
  
  # find out the length of the cycle
  m = 1
  pointer = n
  while pointer!=curr:
    pointer = arr[pointer-1]
    m += 1
    
  print(pointer, m)
  
  # enter cycle
  begin = n
  for _ in range(m):
    begin = arr[begin-1]
  
  
  # find the beginning of the cycle 
  end = n
  while begin!=end:
    end=arr[end-1]
    begin=arr[begin-1]
    
  return begin

print(find_dups_beast_mode([1,4,3,4,2]))

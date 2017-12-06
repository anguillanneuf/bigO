#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:57:08 2017

@author: tz
"""

def find_dups_beast_mode(arr):
<<<<<<< HEAD
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
=======
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
>>>>>>> 6b32cdac606fdf546e518c01fd1e10d5947b9844

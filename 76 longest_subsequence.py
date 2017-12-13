#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:48:21 2017

@author: tz
"""

def longest_subsequence(arr):
  if len(arr) < 2:
    return arr
  
  M = [None for _ in range(len(arr))]
  P = [None for _ in range(len(arr))]
  L = 1
  M[0] = 0
  results = []
  
  for i in range(1,len(arr)):
    # Iterate through input arr
    # First, find j, i.e. where to place i in M. Two cases.
    # Either behind the known largest subsequence, or somewhere inside it.
    
    if arr[i] > arr[M[L-1]]:
      j = L       # If arr[i] exceeds known largest subsequence
    else:         # If arr[i] belongs inside known largest subsequence
      lo=0
      hi=L-1
      while lo+1<hi:
        mid=(lo+hi)//2
        if arr[i]>arr[M[mid]]:
          lo=mid+1
        else:
          hi=mid
      j=lo
      
    
    P[i]=M[j-1]   # Updates P[i], index of the value that leads to arr[i]
    M[j]=i        # Updates M[j], i.e. places i in M
    L=max(L,j+1)  # Updates L
  
  
  k = M[L-1]  
  for _ in range(L):
    results.append(arr[k])
    k=P[k]
    
  return results[::-1]

arr = [30,10,20,50,40,60]
print(longest_subsequence(arr))
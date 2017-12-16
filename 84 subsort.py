# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:40:21 2017

@author: harrisot
"""

def subsort(arr):
  
  n=len(arr)
  left=0
  
  for i in range(n):
    if i==0: 
      continue
    if arr[i]<arr[i-1]:
      left=i
      break
    
  right=n-1
  for j in range(n-1,-1,-1):
    if j==1:
      continue
    if arr[j-1]>arr[j]:
      right=j-1
      break
  
  lmax=max([arr[w] for w in range(left-1,right+1)])
  rmin=min([arr[w] for w in range(left,right+2)])
  
  for i in range(left-1,-1,-1):
    if arr[i]<=rmin:
      left = i+1
      break
    
  for j in range(right+1,n,1):
    if arr[j]>=lmax:
      right=j-1
      break
  
  return left,right


arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subsort(arr)) # 3,9
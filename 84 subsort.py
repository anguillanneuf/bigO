# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:40:21 2017

@author: harrisot
"""
def expand(i,j,arr):
  if i==0 or j==len(arr)-1:
    return (0,len(arr)-1)
  
  lmax=max([arr[w] for w in range(j)])
  rmin=min([arr[w] for w in range(i,len(arr))])
  
  if lmax <= arr[j+1] and rmin >= arr[i-1]:
    return (i,j)
  
  i0,j0=expand(i-1,j,arr)
  i1,j1=expand(i,j+1,arr)
  i2,j2=expand(i-1,j+1,arr)
  
  return min((i0,j0),(i1,j1),(i2,j2),key=lambda a:a[1]-a[0])


def subsort(arr):
  n=len(arr)
  
  for i in range(n):
    if i==0: 
      continue
    if arr[i]<arr[i-1]:
      left=i
      break
  
  for j in range(n-1,-1,-1):
    if j==1:
      continue
    if arr[j-1]>arr[j]:
      right=j-1
      break
  
  return expand(left,right,arr)


arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subsort(arr)) # 3,9
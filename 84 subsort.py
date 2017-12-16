# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:40:21 2017

@author: harrisot
"""

def subsort(arr):
  n=len(arr)
  lj=0
  for i in range(n):
    if i==0: 
      continue
    if arr[i]<arr[i-1]:
      lj=i
      break
    
  ri=n-1
  for i in range(n-1,-1,-1):
    if i==1:
      continue
    if arr[i-1]>arr[i]:
      ri=i
      break

  lmax=max([arr[i] for i in range(ri)])
  rmin=min([arr[i] for i in range(lj,len(arr))])
  print(lj, ri, lmax, rmin)
  
  while lmax >= arr[ri] and rmin <= arr[lj]:
      lj-=1
      ri+=1
      lmax = max([arr[i] for i in range(ri)])
      rmin = min([arr[i] for i in range(lj,len(arr))])
      print(lj, ri, lmax, rmin)

  return (lj,ri)
  


arr = [1,2,4,7,10,11,7,12,6,7,16,18,19]
print(subsort(arr)) # 3,9